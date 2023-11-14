import time
from queue import Queue, Empty
from typing import Dict, Any, List
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish
from langchain.schema.output import LLMResult

class EventTracer(BaseCallbackHandler):

    def __init__(self) :
        super(EventTracer, self).__init__()
        self.traceQueue = Queue(maxsize=10000)
    
    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        message = {
            'type': "Chain",
        }
        #self.traceQueue.put_nowait(message)

    def on_chain_end(
        self, outputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        message = {
            'type': "Chain",
        }
        #self.traceQueue.put_nowait(message)

    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> Any:
        message = {
            'type': "Tool",
            'message': f"invoking  tool '{serialized['name']}'..."
        }
        self.traceQueue.put_nowait(message)

    def on_tool_end(
        self, output : str, **kwargs: Any
    ) -> Any:
        message = {
            'type': "Tool",
            'message': f"[answer] {str(output)}"
        }
        self.traceQueue.put_nowait(message)

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        thought = action.log[:action.log.find('\n')]
        message = {
            'type': "Thought",
            'thought': f"{thought}",
            'action': f"{action.tool}",
            'actionInput': f"{action.tool_input}"
        }
        self.traceQueue.put_nowait(message)

    def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> Any:
        thought = finish.log[:finish.log.find('\n')]
        message = {
            'type': "Answer",
            'thought': f"{thought}",
            'answer': f"{finish.return_values['output']}"
        }
        self.traceQueue.put_nowait(message)

    def get_trace(self, timeout=None) -> str :
        message = { 'type': 'None'}
        try:
            message = self.traceQueue.get(block=True, timeout=timeout)
        except Empty:
            pass
        return message

class StatsCollector(BaseCallbackHandler) :

    def __init__(self) :
        super(StatsCollector, self).__init__()
        self.agentProcessingTime = 0.0
        self.llmCallTimeList = []
        self.toolCallTimeList = []
        self.agentStartTime = 0.0
        self.toolStartTime = 0.0
        self.llmStartTime = 0.0

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        self.llmStartTime = time.time()
    
    def on_llm_end(
        self, response : LLMResult, **kwargs: Any
    ) -> Any:
        self.llmCallTimeList.append(time.time() - self.llmStartTime)
    
    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> Any:
        self.toolStartTime = time.time()

    def on_tool_end(
        self, output : str, **kwargs: Any
    ) -> Any:
        self.toolCallTimeList.append(time.time() - self.toolStartTime)
    
    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        if self.agentStartTime <= 0.0 :
            self.agentStartTime = time.time()

    def on_chain_end(
        self, outputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        self.agentProcessingTime = time.time() - self.agentStartTime

    def collectReset(self) :
        total_llm_time = 0.0
        for e in self.llmCallTimeList:
            total_llm_time += e
        
        total_tool_time = 0.0
        for t in self.toolCallTimeList:
            total_tool_time += t

        stats = {
            'llm_call_count': len(self.llmCallTimeList),
            'llm_time_spent': f"{round(total_llm_time, 2)} sec",
            'tool_call_count': len(self.toolCallTimeList),
            'tool_time_spent': f"{round(total_tool_time, 2)} sec",
            'agent_answer_time': f"{round(self.agentProcessingTime, 2)} sec",
        }

        # reset
        self.agentProcessingTime = 0.0
        self.llmCallTimeList = []
        self.toolCallTimeList = []
        self.agentStartTime = 0.0
        self.toolStartTime = 0.0
        self.llmStartTime = 0.0

        # return
        return stats

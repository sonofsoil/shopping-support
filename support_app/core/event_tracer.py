import json
from queue import Queue, Empty
from typing import Dict, Union, Any, List
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import tracing_enabled
from langchain.llms import OpenAI
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

class LLMTracer(BaseCallbackHandler) :

    def __init__(self) :
        super(LLMTracer, self).__init__()
        self.traceQueue = Queue(maxsize=10000)

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        #self.traceQueue.put_nowait(f"<p><b>LLM</b>: Invoking {serialized['name']}")
        pass
    
    def on_llm_end(
        self, response : LLMResult, **kwargs: Any
    ) -> Any:
        #self.traceQueue.put_nowait(f"<p><b>LLM</b>: Invoking {serialized['name']}")
        pass

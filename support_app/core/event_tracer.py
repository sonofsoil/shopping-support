from queue import Queue, Empty
from typing import Dict, Union, Any, List
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import tracing_enabled
from langchain.llms import OpenAI
from langchain.schema.output import LLMResult

counter = 0

class EventTracer(BaseCallbackHandler):

    def __init__(self) :
        super(EventTracer, self).__init__()
        self.traceQueue = Queue(maxsize=10000)
    
    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        #global trace_queue
        #trace_queue.put_nowait(f"<p>Entering new AgentExecutor Chain...</p>")
        pass

    def on_chain_end(
        self, outputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        #global trace_queue
        #trace_queue.put_nowait(f"<p>Exiting AgentExecutor chain...</p>")
        pass

    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> Any:
        global trace_queue
        self.traceQueue.put_nowait(f"<b>Tool:</b> Invoking {serialized['name']}...")

    def on_tool_end(
        self, output : str, **kwargs: Any
    ) -> Any:
        global trace_queue
        self.traceQueue.put_nowait(f"<b>Tool:</b> Received answer...")

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        thought = action.log[:action.log.find('\n')]
        global trace_queue
        self.traceQueue.put_nowait(f"<b>Thought:</b> {thought}<br>")
        self.traceQueue.put_nowait(f"<b>Next Tool:</b> {action.tool}<br>")
        self.traceQueue.put_nowait(f"<b>Tool Input:</b> {action.tool_input}")

    def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> Any:
        thought = finish.log[:finish.log.find('\n')]
        global trace_queue
        self.traceQueue.put_nowait(f"<b>Thought:</b> {thought}<br>")
        self.traceQueue.put_nowait(f"<b>Final Answer:</b> {finish.return_values['output']}")

    def get_trace(self, timeout=None) -> str :
        global trace_queue
        global counter
        message = f'...{counter}...'
        counter += 1
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
        #global trace_queue
        #self.traceQueue.put_nowait(f"<p><b>LLM</b>: Invoking {serialized['name']}")
        pass
    
    def on_llm_end(
        self, response : LLMResult, **kwargs: Any
    ) -> Any:
        #global trace_queue
        #self.traceQueue.put_nowait(f"<p><b>LLM</b>: Invoking {serialized['name']}")
        pass

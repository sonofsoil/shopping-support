from typing import Dict, Union, Any, List
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import tracing_enabled
from langchain.llms import OpenAI
from langchain.schema.output import LLMResult

class OrderQueryAgentCallbackHandler(BaseCallbackHandler):

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        print(f"[@@@@@@@@@@@@@@@@@] on_chain_start")
        #pass

    def on_chain_end(
        self, outputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        print(f"[@@@@@@@@@@@@@@@@@] on_chain_end")
        #pass

    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> Any:
        print(f"[@@@@@@@@@@@@@@@@@] Invoking the tool: {serialized['name']}")

    def on_tool_end(
        self, output : str, **kwargs: Any
    ) -> Any:
        print(f"[@@@@@@@@@@@@@@@@@] Finishing the tool: {output}")

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        thought = action.log[:action.log.find('\n')]
        print(f"[@@@@@@@@@@@@@@@@@] Thought: {thought}")
        print(f"[@@@@@@@@@@@@@@@@@] Next Tool: {action.tool}")
        print(f"[@@@@@@@@@@@@@@@@@] Tool Input: {action.tool_input}")

    def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> Any:
        thought = finish.log[:finish.log.find('\n')]
        print(f"[@@@@@@@@@@@@@@@@@] Thought: {thought}")
        print(f"[@@@@@@@@@@@@@@@@@]: Answer: {finish.return_values['output']}")


class LLMCallbackHandler(BaseCallbackHandler):
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        print(f"[@@@@@@@@@@@@@@@@@] on_llm_start")
        #pass
    
    def on_llm_end(
        self, response : LLMResult, **kwargs: Any
    ) -> Any:
        print(f"[@@@@@@@@@@@@@@@@@] on_llm_end")
        #pass

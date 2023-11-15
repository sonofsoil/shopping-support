from queue import Queue
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from support_app.core.prompt_templates import order_query_prompt_str
from support_app.core.tool_registry import SupportTools
from langchain.prompts import PromptTemplate
from datetime import datetime
import langchain
from langchain.callbacks.manager import CallbackManager
from support_app.core.event_tracer import EventTracer, StatsCollector
from support_app.core.llm_provider import get_gpt_35_llm

langchain.debug=False

# query = """When is my order is scheduled for delivery?
#            It is a small flower vase for holding a bunch of roses.
#            If order not delivered in next two days, please cancel my order.
#          """

def answer_order_query(user_id : str,
                       user_query : str,
                       tracer : EventTracer,
                       stats_collector : StatsCollector) -> str :
    """The order expert can handle any order related query from the
    user. The query can be the current status of an order, expected
    delivery date etc. It can cancel the existing order as appropriate.

    :param user_id: the user identifier of the user
    :param user_query: the order related query from the user
    :param tracer: Agent event trace capture callback
    :param stats_collector: agent stats collector
    :return: the answer to the user query
    """

    now = datetime.now() # current date and time
    # agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    agent = initialize_agent(
        tools = SupportTools().get_tools(),
        llm = get_gpt_35_llm(),
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True)

    prompt_template = PromptTemplate.from_template(order_query_prompt_str)

    prompt = prompt_template.format(
        user_id=user_id,
        current_date=now.strftime("%B %d, %Y"),
        input=user_query
    )
    return agent.run(prompt, callbacks=[tracer, stats_collector])

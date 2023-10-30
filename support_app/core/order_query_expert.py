from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from support_app.core.tools import fetch_orders, cancel_order
from support_app.core.prompt_templates import order_query_prompt_str
from langchain.prompts import PromptTemplate
from datetime import datetime
from langchain.tools import StructuredTool
from support_app.core.order_tracker_expert import derive_days_to_deliver
from support_app.core.order_cancel_expert import decide_cancel_order
from support_app.core.order_identifier_expert import identify_relevant_order
import langchain

langchain.debug=False
model = "gpt-3.5-turbo"
temperature = 0.1

# query = """When is my order is scheduled for delivery?
#            It is a small flower vase for holding a bunch of roses.
#            If order not delivered in next two days, please cancel my order.
#          """

def answer_order_query(user_id : str, user_query : str) -> str :
    """The order expert can handle any order related query from the
    user. The query can be the current status of an order, expected
    delivery date etc. It can cancel the existing order as appropriate.

    :param user_id: the user identifier of the user
    :param user_query: the order related query from the user
    :return: the answer to the user query
    """

    fetch = StructuredTool.from_function(fetch_orders)
    single = StructuredTool.from_function(identify_relevant_order)
    ddiff = StructuredTool.from_function(derive_days_to_deliver)
    decide = StructuredTool.from_function(decide_cancel_order)
    cancel = StructuredTool.from_function(cancel_order)

    now = datetime.now() # current date and time
    # agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    llm = OpenAI(model_name=model, temperature=temperature) # Also works well with Anthropic models
    agent = initialize_agent(
        tools = [fetch, single, ddiff, decide, cancel],
        llm = llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True)

    prompt_template = PromptTemplate.from_template(order_query_prompt_str)

    prompt = prompt_template.format(
        user_id=user_id,
        current_date=now.strftime("%B %d, %Y"),
        input=user_query
    )
    return agent.run(prompt)

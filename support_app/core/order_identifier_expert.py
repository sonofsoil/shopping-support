from langchain.llms import OpenAI
from support_app.core.prompt_templates import order_identifier_prompt_str
from langchain.prompts import PromptTemplate
from support_app.core.llm_provider import get_gpt_35_llm

def identify_relevant_order(user_query : str, order_list : str) -> str :
    """ Finds and returns the matching order from the user query and
    the list of orders.
    :param user_query: user query
    :param order_list: List of order details for the user; json list
    :return: matching order in json structure
    """

    llm = get_gpt_35_llm()
    prompt_template = PromptTemplate.from_template(order_identifier_prompt_str)
    prompt = prompt_template.format(
        user_query=user_query,
        order_list=order_list)
    out = llm.predict(prompt)
    return out

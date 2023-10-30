from langchain.llms import OpenAI
from support_app.core.prompt_templates import order_cancellation_decision_prompt_str
from langchain.prompts import PromptTemplate

model = "gpt-3.5-turbo"
temperature = 0.1

def decide_cancel_order(user_query : str, days_to_deliver : str) -> str :
    """ Given the user query and number of days to deliver
    the order,decides whether the order need to be canceled.
    :param user_query: user query
    :param days_to_deliver: number of days to deliver the order.
    :return: whetjer the order needs to be canceled.
    """

    llm = OpenAI(model_name=model, temperature=temperature)
    prompt_template = PromptTemplate.from_template(order_cancellation_decision_prompt_str)
    prompt = prompt_template.format(
        user_query=user_query,
        days=days_to_deliver)
    #print(prompt)
    return llm.predict(prompt)
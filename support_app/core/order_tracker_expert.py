import json
from langchain.llms import OpenAI
from support_app.core.prompt_templates import date_time_diff_prompt_str
from langchain.prompts import PromptTemplate
from support_app.core.llm_provider import get_gpt_35_llm

def derive_days_to_deliver(current_date : str, delivery_date: str) -> str:
    """ Given current date and time as well as delivery date and
    time, ccalculates the number of days and hours for a delivery
    from current date and time.
    :param current_date: current date
    :param delivery_date: delivery date
    :return: number of days and hours remaining for delivery.
    """

    llm = get_gpt_35_llm()
    prompt_template = PromptTemplate.from_template(date_time_diff_prompt_str)
    prompt = prompt_template.format(
        current_date=current_date, delivery_date=delivery_date)
    #print(prompt)
    response = llm.predict(prompt)
    diff = json.loads(response)
    if diff['days']  > 0:
        return f"order is delivering in {diff['days']} days"
    return f"order already delivered"

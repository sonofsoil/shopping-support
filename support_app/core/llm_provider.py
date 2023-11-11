from langchain.llms import OpenAI
from support_app.core.event_tracer import LLMTracer

model = "gpt-3.5-turbo"
temperature = 0.1

def get_gpt_35_llm() -> OpenAI :
    return OpenAI(model_name=model,
                  streaming=True,
                  temperature=temperature,
                  callbacks=[LLMTracer()])
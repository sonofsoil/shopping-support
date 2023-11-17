from langchain.llms import OpenAI

#model = "gpt-3.5-turbo"
model = "gpt-4"
temperature = 0.1

def get_gpt_35_llm() -> OpenAI :
    return OpenAI(model_name=model,
                  streaming=True,
                  temperature=temperature,
                  callbacks=[])

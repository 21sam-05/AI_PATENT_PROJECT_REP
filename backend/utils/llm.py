import google.generativeai as genai

genai.configure(api_key="you-api-key")
# for m in genai.list_models():
#     print(m.name)

def get_llm():

    model = genai.GenerativeModel("gemini-2.5-flash")

    return model

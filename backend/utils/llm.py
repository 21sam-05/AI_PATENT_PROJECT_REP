import google.generativeai as genai

genai.configure(api_key="AIzaSyAjpGvc8bR6wm2va3uF7mn46vhgxT3uAwg")
# for m in genai.list_models():
#     print(m.name)

def get_llm():

    model = genai.GenerativeModel("gemini-2.5-flash")

    return model
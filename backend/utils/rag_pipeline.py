from utils.retriever import search_patent
from utils.llm import get_llm

def ask_question(query):

    retrieved_docs = search_patent(query)

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    prompt = f"""
    You are an AI Patent Assistant.

    Use the following patent context to answer.

    Context:
    {context}

    Question:
    {query}
    """

    model = get_llm()

    response = model.generate_content(prompt)

    return response.text
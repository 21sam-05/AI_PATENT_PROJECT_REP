from langchain_community.vectorstores import FAISS
from utils.embeddings import get_embedding_model

VECTOR_DB_PATH = "vectordb"


def search_similar_patents(query, k=5):

    embedding_model = get_embedding_model()

    vector_store = FAISS.load_local(
        VECTOR_DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    results = vector_store.similarity_search_with_score(query, k=k)

    return results
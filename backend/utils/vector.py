import os

from langchain_community.vectorstores import FAISS

VECTOR_DB_PATH = "vectordb"


def create_vector_store(chunks, embedding_model):

    if len(chunks) == 0:
        raise ValueError("No chunks created from PDF.")

    if os.path.exists(VECTOR_DB_PATH):

        vector_store = FAISS.load_local(
            VECTOR_DB_PATH,
            embedding_model,
            allow_dangerous_deserialization=True
        )

        vector_store.add_documents(chunks)

    else:

        vector_store = FAISS.from_documents(
            chunks,
            embedding_model
        )

    vector_store.save_local(VECTOR_DB_PATH)

    return vector_store
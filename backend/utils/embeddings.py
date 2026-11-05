from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embedding_model():

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    return embedding_model





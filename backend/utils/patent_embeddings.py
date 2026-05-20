##create embedding vectors for patent text

from utils.embeddings import get_embedding_model


embedding_model = get_embedding_model()


def get_patent_embedding(text):

    embedding = embedding_model.embed_query(text)

    return embedding
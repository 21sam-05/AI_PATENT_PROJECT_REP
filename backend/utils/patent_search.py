
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy

from utils.embeddings import get_embedding_model


VECTOR_DB_PATH = Path(__file__).resolve().parent.parent / "vectordb"


def search_similar_patents(query, k=5):

    if not VECTOR_DB_PATH.exists():
        raise FileNotFoundError(
            "Patent vector database not found. Upload a patent first."
        )

    embedding_model = get_embedding_model()

    vector_store = FAISS.load_local(
        str(VECTOR_DB_PATH),
        embedding_model,
        allow_dangerous_deserialization=True,
        distance_strategy=DistanceStrategy.MAX_INNER_PRODUCT
    )

    results = vector_store.similarity_search_with_score(
        query,
        k=k
    )

    return results
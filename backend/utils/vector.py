
from pathlib import Path
from faiss import IndexFlatIP
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
from langchain_community.docstore.in_memory import InMemoryDocstore


VECTOR_DB_PATH = Path(__file__).resolve().parent.parent / "vectordb"


def create_vector_store(chunks, embedding_model):

    if not chunks:
        raise ValueError("No chunks created from PDF.")

    if VECTOR_DB_PATH.exists():

        vector_store = FAISS.load_local(
            str(VECTOR_DB_PATH),
            embedding_model,
            allow_dangerous_deserialization=True,
            distance_strategy=DistanceStrategy.MAX_INNER_PRODUCT
        )

        vector_store.add_documents(chunks)

    else:

        dimension = len(embedding_model.embed_query("test"))

        index = IndexFlatIP(dimension)

        vector_store = FAISS(
            embedding_model,
            index,
            InMemoryDocstore({}),
            {},
            normalize_L2=False,
            distance_strategy=DistanceStrategy.MAX_INNER_PRODUCT
        )

        vector_store.add_documents(chunks)

    vector_store.save_local(str(VECTOR_DB_PATH))

    return vector_store
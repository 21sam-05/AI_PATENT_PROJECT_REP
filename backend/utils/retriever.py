##now we retrieve relevant patents 
# allow for similarity
#  
##as they are mebedded now we will do semantic search

from langchain_community.vectorstores import FAISS
from utils.embeddings import get_embedding_model


##load my saved knowledge 
#base so I  can searchh similar docs
def load_vector_store():
    embedding_model=get_embedding_model()
    vector_store=FAISS.load_local(
        "vectordb",
        embedding_model,
        allow_dangerous_deserialization=True
    )
    return vector_store

def search_patent(query):
    vector_store=load_vector_store()

    results=vector_store.similarity_search(
        query,
        k=5
    )

    return results




from utils.patent_embeddings import get_patent_embedding
from utils.similarity import calculate_similarity


def compare_patents(text1, text2):

    embedding1 = get_patent_embedding(text1)

    embedding2 = get_patent_embedding(text2)

    similarity_score = calculate_similarity(
        embedding1,
        embedding2
    )

    return round(similarity_score * 100, 2)

##converts patent A->vector
##converts patent B-> VECTOR
##compare and return percentage similarity

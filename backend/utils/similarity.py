from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(embedding1,embedding2):
    similarity=cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

    return similarity
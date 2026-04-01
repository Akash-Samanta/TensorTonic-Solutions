import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    # Write code here
    k = min(k, len(relevance_scores))

    def dcg(scores):
        total = 0.0 
        for i, rel in enumerate(scores[:k]):
            gain = (2 ** rel) - 1
            discount = math.log(i + 2)
            total += gain / discount 
        return total 

    dcg_val = dcg(relevance_scores)

    ideal_scores = sorted(relevance_scores, reverse=True)
    idcg_val = dcg(ideal_scores)

    if idcg_val == 0:
        return 0.0 

    return dcg_val / idcg_val
import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / max((np.linalg.norm(a) * np.linalg.norm(b)), 1e-12)
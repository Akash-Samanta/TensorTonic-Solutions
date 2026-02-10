import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    h, w = A.shape 
    at = np.zeros((w, h))

    for i in range(h):
        for j in range(w):
            at[j, i] = A[i, j]
    return at

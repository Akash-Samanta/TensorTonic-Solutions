import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    n = len(A)
    s = 0
    for i in range(n):
      s+= A[i][i]
    return s
      

import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    return [
        (np.exp(i) - np.exp(-i)) / (np.exp(i) + np.exp(-i))
        for i in x
    ]
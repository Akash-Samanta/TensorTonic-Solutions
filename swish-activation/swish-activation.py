import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.array(x)
    return [
        i / (1 + np.exp(-i))
        for i in x
    ]
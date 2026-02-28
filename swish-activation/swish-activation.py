import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
  
    return [
        i / (1 + np.exp(-i))
        for i in np.array(x)
    ]
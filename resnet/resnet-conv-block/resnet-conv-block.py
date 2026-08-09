import numpy as np

def relu(x):
    return np.maximum(0, x)

def conv_block(x, W1, W2, Ws):
    """
    Returns: np.ndarray with sum of main path output and projected shortcut
    """
    # YOUR CODE HERE
    x, W1, W2, Ws = map(np.asarray, (x, W1, W2, Ws))
    shortcut = x @ Ws 
    out = relu(x @ W1)
    out = out @ W2
    return relu(out + shortcut)


    

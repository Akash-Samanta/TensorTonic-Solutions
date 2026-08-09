import numpy as np

def identity_block(x, W1, W2):
    """
    Returns: np.ndarray of shape (batch, channels) with identity residual block output
    """
    # YOUR CODE HERE
    h = np.maximum(0, x @ np.transpose(W1))
    y = np.maximum(0, h @ np.transpose(W2) + x)
    return y

import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.array(x)
    keep = 1 - p 
    if rng is not None:
        ran = rng.random(x.shape)
    else:
        ran = np.random.random(x.shape)
    dropout_pattern = (ran < keep).astype(x.dtype) / keep 
    output = x * dropout_pattern
    return output, dropout_pattern
    
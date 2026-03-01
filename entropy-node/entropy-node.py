import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if y is None or len(y) == 0:
        return 0.0 

    _, counts = np.unique(y, return_counts=True)
    prob = counts / counts.sum()
    prob = prob[prob > 0]
    entropy = -np.sum(prob * np.log2(prob))
    return entropy
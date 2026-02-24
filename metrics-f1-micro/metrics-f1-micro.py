import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_true, y_pred = np.array(y_true), np.array(y_pred)

    tp = np.sum(y_true == y_pred)
    
    return float(tp) / len(y_true)
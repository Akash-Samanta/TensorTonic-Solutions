import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    m = float(np.mean(x))
    mm = float(np.median(x))
    counts = Counter(x)
    max_freq = max(counts.values())
    mmm = min(k for k, v in counts.items() if v == max_freq)
    return m, mm, mmm

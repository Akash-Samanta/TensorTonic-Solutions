import numpy as np

def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    arr = np.array(values, dtype=float)
    n = len(arr)

    if n == 1:
        return [0.0]

    sorted_arr = sorted(arr)
    median = np.median(sorted_arr)

    mid = n // 2 

    if n%2 == 0:
        lower = sorted_arr[:mid]
        upper = sorted_arr[mid:]
    else:
        lower = sorted_arr[:mid]
        upper = sorted_arr[mid+1:]

    q1 = np.median(lower)
    q3 = np.median(upper)

    iqr = q3 - q1 

    if iqr == 0:
        return (arr - median).tolist()
    return ((arr - median) / iqr).tolist()

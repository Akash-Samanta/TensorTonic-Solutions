from statistics import median

def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    return [
        median(values[i: i+window_size])
        for i in range(len(values)- window_size + 1)
    ]
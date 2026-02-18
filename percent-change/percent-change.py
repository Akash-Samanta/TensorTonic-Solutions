def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    return [
        (series[i] - series[i-1]) / series[i-1] if series[i-1]!= 0 else 0 
        for i in range(1, len(series))
    ]
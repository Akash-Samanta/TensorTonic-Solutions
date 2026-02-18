def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    for o in range(order):
        cop = series 
        temp = []
        for i in range(1, len(cop)):
            temp.append(cop[i] - cop[i-1])
        series = temp 
    return series
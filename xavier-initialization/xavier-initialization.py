def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    limit = (6 / (fan_in + fan_out)) ** 0.5 
    W = np.array(W)
    return W * 2 * limit - limit
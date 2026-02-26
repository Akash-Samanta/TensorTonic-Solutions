def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    X, W, b = np.array(X), np.array(W), np.array(b)
    return (X @ W + b).tolist()
import numpy as np

def alexnet_conv1(image: np.ndarray) -> np.ndarray:
    """AlexNet first conv layer: 11x11, stride 4, 96 filters (shape simulation)."""
    # YOUR CODE HERE
    
    kernel_size = 11 
    stride = 4 
    padding = 2 
    num_filters = 96

    n, h, w, c = image.shape 
    
    h_out = (h + 2 * padding - kernel_size ) // stride + 1 
    w_out = (w + 2 * padding - kernel_size ) // stride + 1 
    return np.zeros((n, h_out, w_out, num_filters))
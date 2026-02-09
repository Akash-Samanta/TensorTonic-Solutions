import numpy as np

def morphological_op(image, kernel, operation):
    """
    Apply morphological erosion or dilation to a binary image.
    """
    # Write code here
    image = np.array(image)
    kernel = np.array(kernel)
    h, w = image.shape
    kh, kw = kernel.shape
    pad_h, pad_w = kh // 2, kw // 2 

    padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
    output = np.zeros((h, w), dtype=int)

    for i in range(h):
        for j in range(w):
            region = padded[i:i+kh, j:j+kw]

            masked = region[kernel==1]

            if operation == 'erode':
                output[i, j] = int(np.all(region[kernel==1]==1))
            elif operation == 'dilate':
                output[i, j] = int(np.any(region & kernel))

    return output.tolist()

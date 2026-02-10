import numpy as np

def sobel_edges(image):
    """
    Apply the Sobel operator to detect edges.
    """
    # Write code here

    img = np.array(image, dtype=float)
    Kx = np.array([
        [-1,  0,  1],
        [-2,  0,  2],
        [-1,  0,  1]
    ], dtype=float)

    Ky = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ], dtype=float)

    h, w= img.shape 
    padded = np.pad(img, pad_width=1, mode='constant', constant_values=0)
    gx = np.zeros((h, w))
    gy = np.zeros((h, w))

    for i in range(h):
        for j in range(w):
            patch = padded[i:i+3, j:j+3]
            gx[i, j] = np.sum(patch * Kx)
            gy[i, j] = np.sum(patch * Ky)

    magnitude = np.sqrt(gx**2 + gy**2)
    return magnitude.tolist()
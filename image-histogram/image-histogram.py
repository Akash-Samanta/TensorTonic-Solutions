def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    h = [0] * 256 
    for i in range(len(image)):
        for j in range(len(image[0])):
            h[image[i][j]] += 1
    return h
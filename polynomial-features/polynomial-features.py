import numpy as np

def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    values = np.array(values)[:, None]
    degree = np.arange(degree+1)
    return (values ** degree).tolist()
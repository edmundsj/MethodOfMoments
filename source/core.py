import numpy as np
from physicalConstants import *

# Exact solution to the diagonal terms for the method of moments
def La(rectangleRadius):
    return np.reciprocal(4*np.pi*epsilon0*rectangleRadius) * \
            (np.log(1 + np.sqrt(2)) - np.log(np.sqrt(2) - 1))

def Lself(rectangleRadius):
    return np.reciprocal(rectangleRadius) * (np.log(1 + np.sqrt(2)) - np.log(np.sqrt(2) - 1))

# Empirical off-diagonal terms Lij
def Lij(rectangleRadius, vector1, vector2):
    # we can vectorize this function to use with meshgrid by grabbing the vector components explicitly
    r = np.sqrt(np.square(vector1[0]-vector2[0]) + \
            np.square(vector1[1] - vector2[1]) + \
            np.square(vector1[2] - vector2[2]))
    return np.reciprocal(4*np.pi*epsilon0) * 1 / (r + 1/(Lself(rectangleRadius)*(1+r/rectangleRadius)))

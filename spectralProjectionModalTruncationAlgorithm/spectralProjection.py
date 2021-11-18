import numpy as np

def calculateSpectralProjection(A, I, alpha):
    P = np.sign(A + alpha.dot(I))
    return P
import numpy as np

def calculateSpectralProjection(A: np.ndarray, I: np.ndarray, alpha: np.ndarray):
    P = np.sign(A + alpha.dot(I))
    return P
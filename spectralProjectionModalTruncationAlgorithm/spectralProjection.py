import numpy as np

def calculateSpectralProjection(A: np.ndarray, alpha: np.ndarray):
    I = np.identity(np.shape(A)[0])
    P = np.sign(A + (alpha * I))
    
    return P
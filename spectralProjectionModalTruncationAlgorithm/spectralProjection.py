import numpy as np

def calculateSpectralProjection(A: np.ndarray, alpha: np.ndarray):
    I = np.identity(np.shape(A)[0])
    P = 1/2 * (I + np.sign(A + (alpha * I)))
    
    return P
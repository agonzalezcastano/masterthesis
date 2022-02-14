import numpy as np

def calculateSpectralProjection(A: np.ndarray, alpha: np.ndarray):
    I = np.identity(np.shape(A)[0])
    sign = np.sign(A + (alpha * I))
    P_ = 1/2 * (I - sign)
    
    return P_
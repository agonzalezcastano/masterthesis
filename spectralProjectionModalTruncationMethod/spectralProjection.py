import numpy as np
import scipy.linalg as linalg

def calculateSpectralProjection(A: np.ndarray, alpha: np.ndarray):
    I = np.identity(np.shape(A)[0])
    new_A = A + (alpha * I)
    sign = np.sign(new_A)
    P_ = 1/2 * (I - sign)
    
    return sign
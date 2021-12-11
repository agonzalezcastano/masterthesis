import numpy as np
import numpy.linalg as linalg

def computeBeta(A: np.ndarray):
    eigen_values: np.ndarray = linalg.eigvals(A)
    real = eigen_values.real
    beta = max(real)
    return beta
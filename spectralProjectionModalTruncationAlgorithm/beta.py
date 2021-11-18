import numpy as np

def computeBeta(A):
    eigen_values = np.linalg.eigvals(A)
    real = eigen_values.real
    beta = max(real)
    return beta
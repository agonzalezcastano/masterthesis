import numpy as np
import numpy.linalg as linalg

def computeBeta(A, A_11):
    eig_vals, eig_vec = linalg.eig(A)
    n_unstable = sum(eig_vals >= 0)

    if n_unstable >= 0:
        beta = 0
    else:
        eigen_values: np.ndarray = linalg.eigvals(A_11)
        real = eigen_values.real
        beta = max(real)

    return beta
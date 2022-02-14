from matplotlib.pyplot import axis
import numpy as np
from numpy.linalg import linalg
import scipy.linalg as scilinalg

def calculateProjectionMatrixQ(A: np.ndarray, C: np.ndarray):
    trasC = np.transpose(C)
    T = -trasC @ C
    trasA = np.transpose(A)
    Q = scilinalg.solve_continuous_lyapunov(trasA, T)

    return Q

def calculateProjectionMatrixV(A: np.ndarray, B: np.ndarray, interpolation_points: np.ndarray, reduced_order):
    A_height = A.shape[0]
    I = np.identity(A_height)
    V_weight = reduced_order
    V: np.ndarray = np.empty((A_height, V_weight), dtype='complex')
    k = 0

    num = 0
    # Initilize for first interpolation point
    M = linalg.pinv(A - (interpolation_points[num] * I))
    R = M @ B

    v_1 = B/linalg.norm(B)
    w = M @ v_1

    alpha_1 = v_1 @ linalg.transpose(w)
    f_i = w - (alpha_1 @ v_1)

    V = np.append(V, v_1, axis=1)

    for num in range(1, np.shape(interpolation_points)[0], 1):
        beta_i = linalg.norm(f_i)
        v_next = f_i/beta_i
        V = np.append(V, v_next, axis=1)

    V = np.imag(V)

    return V

def calculateProjectionMatrixZ(Q: np.ndarray, V: np.ndarray):
    trasV = V.transpose()
    inv = linalg.pinv(trasV @ Q @ V)
    Z = Q @ V @ inv

    return Z
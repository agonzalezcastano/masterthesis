import numpy as np
from numpy.linalg import linalg
import scipy.linalg as scilinalg

def calculateProjectionMatrixQ(A: np.ndarray, C: np.ndarray):
    trasC = C.transpose()
    T = -trasC.dot(C)
    trasA = A.transpose()
    Q = scilinalg.solve_continuous_lyapunov(trasA, T)
    return Q

def calculateProjectionMatrixV(A: np.ndarray, B: np.ndarray, interpolation_points: np.ndarray):
    A_height = A.shape[0]
    I = np.identity(A_height)
    V_weight = np.shape(B)[1] * np.shape(interpolation_points)[0]
    V: np.ndarray = np.zeros((A_height, V_weight), dtype='complex')
    k = 0

    for num in range(0, np.shape(interpolation_points)[0], 1):
        E = (interpolation_points[num] * I) - A
        F = linalg.pinv(E)
        v = np.dot(F, B)
        v_temp: np.ndarray = v/linalg.norm(v)
        v_next, r = linalg.qr(v_temp)
        v_temp: np.ndarray = v_next/linalg.norm(v_next)
        V[:, 0] = v_temp[:, 0]
        for i in range(1, np.shape(B)[1], 1):
            V[:, k + i] = v_temp[:, i]
        k = num + 2
        
    V = np.real(V)
    return V

def calculateProjectionMatrixZ(Q: np.ndarray, V: np.ndarray):
    trasV = V.transpose()
    inv = linalg.pinv(trasV.dot(Q).dot(V))
    Z = Q.dot(V).dot(inv)
    return Z
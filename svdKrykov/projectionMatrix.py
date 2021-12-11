import numpy as np
from numpy.linalg import linalg
import scipy.linalg as scilinalg

def calculateProjectionMatrixQ(A: np.ndarray, C: np.ndarray):
    trasC = C.transpose()
    T = -trasC.dot(C)
    trasA = A.transpose()
    Q = scilinalg.solve_continues_lyapunov(trasA, T)
    return Q

def calculateProjectionMatrixV(A: np.ndarray, B: np.ndarray, interpolation_points: np.ndarray):
    A_height = A.shape[0]
    A_weight = A.shape[1]

    I = np.identity(A_height)
    E = np.dot(interpolation_points, I) - A
    F = linalg.inv(E)
    V = np.imag(np.dot(F,B))

    return V

def calculateProjectionMatrixZ(Q: np.ndarray, V: np.ndarray):
    trasV = V.transpose()
    inv = linalg.inv(trasV.dot(Q).dot(V))
    Z = Q.dot(V).dot(inv)
    return Z
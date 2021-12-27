import numpy as np
from numpy.core.fromnumeric import shape
from numpy.lib.type_check import imag
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
    
    E = (interpolation_points[0] * I) - A
    F = linalg.inv(E)
    v = np.dot(F, B)
    v_temp = v/linalg.norm(v)

    for num in range(1, np.shape(interpolation_points)[0], 1):
        print("num")
        print(num)
        E = (interpolation_points[num] * I) - A
        F = linalg.inv(E)
        v = np.dot(F,v_temp)
        v_next, r = linalg.qr(v)
        V = v_next/linalg.norm(v_next)
        v_temp = v_next
        print("shape V inside method")
        print(np.shape(V))

    return V

def calculateProjectionMatrixZ(Q: np.ndarray, V: np.ndarray):
    trasV = V.transpose()
    inv = linalg.inv(trasV.dot(Q).dot(V))
    Z = Q.dot(V).dot(inv)
    return Z
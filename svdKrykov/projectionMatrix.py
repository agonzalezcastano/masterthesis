import numpy as np
import scipy as sci

def calculateProjectionMatrixQ(C):
    trasC = C.transpose()
    T = -trasC.dot(C)
    Q = sci.linalg.solve_
    return Q, T

def calculateProjectionMatrixV(A, B, interpolation_points):
    A_height = A.shape[0]
    A_weight = A.shape[1]
    I = np.identity(A_height)
    E = interpolation_points.dot(I)-A
    F = np.linalg.inv(E)
    V = np.imag(F.dot(B))
    return V

def calculateProjectionMatrixZ(Q, V):
    trasV = V.transpose()
    inv = np.linalg.inv(trasV.dot(Q).dot(V))
    Z = Q.dot(V).dot(inv)
    return Z
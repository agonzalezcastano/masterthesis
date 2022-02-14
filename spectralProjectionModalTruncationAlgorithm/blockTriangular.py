from numpy import ndarray
import decomposeMatrix
import numpy as np

def computeBlockTriangularA(A: ndarray, Q: ndarray):
    Q_t = np.transpose(Q)
    tri_A = Q_t @ A @ Q
    A_11, A_12, A_21, A_22 = decomposeMatrix.decomposeMatrixInFour(tri_A)

    return A_11, A_12, A_21, A_22

def computeBlockTriangularB(B: ndarray, Q: ndarray):
    tri_B = np.transpose(Q) @ B
    B_1, B_2 = decomposeMatrix.decomposeMatrixInTwo(tri_B)

    return B_1, B_2

def computeBlockTriangularC(C: ndarray, Q: ndarray):
    tri_C = C @ Q
    tri_C = np.transpose(tri_C)
    C_1, C_2 = decomposeMatrix.decomposeMatrixInTwo(tri_C)
    C_1 = C_1.transpose()
    C_2 = C_2.transpose()

    return C_1, C_2
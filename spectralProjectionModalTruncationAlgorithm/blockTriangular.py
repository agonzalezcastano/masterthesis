from numpy import ndarray
import numpy as np
import decomposeMatrix

def computeBlockTriangularA(A: ndarray, Q: ndarray):
    tri_A = Q.transpose().dot(A).dot(Q)
    A_11, A_12, A_21, A_22 = decomposeMatrix.decomposeMatrixInFour(tri_A)

    return A_11, A_12, A_21, A_22

def computeBlockTriangularB(B: ndarray, Q: ndarray):
    tri_B = Q.transpose().dot(B)
    B_1, B_2 = decomposeMatrix.decomposeMatrixInTwo(tri_B)

    return B_1, B_2

def computeBlockTriangularC(C: ndarray, Q: ndarray):
    triC = C.dot(Q)
    triC = triC.transpose()
    C_1, C_2 = decomposeMatrix.decomposeMatrixInTwo(triC)
    C_1 = C_1.transpose()
    C_2 = C_2.transpose()

    return C_1, C_2
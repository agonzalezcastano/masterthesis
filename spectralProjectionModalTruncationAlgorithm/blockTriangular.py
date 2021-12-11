from numpy import ndarray
import decomposeMatrix

def computeBlockTriangularA(A: ndarray, Q: ndarray):
    tri_A = Q.transpose().dot(A).dot(Q)
    A_11, A_12, A_21, A_22 = decomposeMatrix.decomposeMatrixInFour(tri_A)

    return A_11, A_12, A_22

def computeBlockTriangularB(B: ndarray, Q: ndarray):
    tri_B = Q.transpose().dot(B)
    B_1, B_2 = decomposeMatrix.decomposeMatrixInTwo(tri_B)

    return B_1, B_2

def computeBlockTriangularC(C: ndarray, Q: ndarray):
    triC = C.dot(Q)
    C_1, C_2 = decomposeMatrix.decomposeMatrixInTwo(triC)

    return C_1, C_2
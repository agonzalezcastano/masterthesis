import numpy as np

def computeReducedMatrixA(A: np.ndarray, Z: np.ndarray, V: np.ndarray):
    tras_Z = Z.transpose()
    A_r = tras_Z.dot(A).dot(V)
    return A_r

def computeReducedMatrixB(B: np.ndarray, Z: np.ndarray):
    tras_Z = Z.transpose()
    B_r = tras_Z.dot(B)
    return B_r

def computeReducedMatrixC(C: np.ndarray, V: np.ndarray):
    C_r = C.dot(V)
    return C_r
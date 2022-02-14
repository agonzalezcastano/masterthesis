import numpy as np

def computeReducedSystem(A, B, C, D, Z, V):
    A_r = computeReducedMatrixA(A, Z, V)
    B_r = computeReducedMatrixB(B, Z)
    C_r = computeReducedMatrixC(C, V)
    D_r = D
    
    return A_r, B_r, C_r, D_r

def computeReducedMatrixA(A: np.ndarray, Z: np.ndarray, V: np.ndarray):
    trans_Z = np.transpose(Z)
    A_r = trans_Z @ A @ V
    return A_r

def computeReducedMatrixB(B: np.ndarray, Z: np.ndarray):
    tras_Z = np.transpose(Z)
    B_r = tras_Z @ B
    return B_r

def computeReducedMatrixC(C: np.ndarray, V: np.ndarray):
    C_r = C @ V
    return C_r
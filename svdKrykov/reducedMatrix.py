import numpy as np

def computeReducedMatrixA(A, Z, V):
    tras_Z = Z.transpose()
    A_r = tras_Z.dot(A).dot(V)
    return A_r

def computeReducedMatrixB(B, Z):
    tras_Z = Z.transpose()
    B_r = tras_Z.dot(B)
    return B_r

def computeReducedMatrixC(C, V):
    C_r = C.dot(V)
    return C_r
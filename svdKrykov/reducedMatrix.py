import numpy as np
from numpy.core.fromnumeric import transpose

def computeReducedMatrixA(A: np.ndarray, Z: np.ndarray, V: np.ndarray):
    trans_Z = Z.transpose()
    I = trans_Z.dot(V)
    print("I")
    print(I)
    print("shape I")
    print(np.shape(I))
    A_r = trans_Z.dot(A).dot(V)
    print("Shape A")
    print(np.shape(A))
    print("Shape Z")
    print(np.shape(Z))
    print("Shape V")
    print(np.shape(V))
    print("Shape A_r")
    print(np.shape(A_r))   
    return A_r

def computeReducedMatrixB(B: np.ndarray, Z: np.ndarray):
    tras_Z = Z.transpose()
    B_r = tras_Z.dot(B)
    return B_r

def computeReducedMatrixC(C: np.ndarray, V: np.ndarray):
    C_r = C.dot(V)
    return C_r
from numpy import ndarray
import decomposeMatrix
import scipy.linalg as la
import numpy as np

def solveSylvesterEquation(A: ndarray, beta: ndarray):
    A_11, A_12, A_21, A_22 = decomposeMatrix.decomposeMatrixInFour(A)

    I = np.identity(np.shape(A_11)[0])
    A = A_11 - (beta * I)
    B = (beta * I) - A_22
    Q = -A_12
    X = la.solve_sylvester(A, B, Q)
    
    return X
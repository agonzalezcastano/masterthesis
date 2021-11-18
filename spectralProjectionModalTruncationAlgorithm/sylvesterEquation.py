import decomposeMatrix
import scipy.linalg as la

def solveSylvesterEquation(A, beta, I):
    A_11, A_12, A_21, A_22 = decomposeMatrix.decomposeMatrixInFour(A)

    A = A_11 - beta.dot(I)
    B = beta.dot(I) - A_22
    Q = -A_12
    X = la.solve_sylvester(A, B, Q)
    
    return X
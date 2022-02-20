import scipy.linalg as la
import numpy as np

def solveSylvesterEquation(A_11, A_12, A_22, beta):
    I = np.identity(np.shape(A_11)[0])
    A = A_11 - (beta * I)
    I = np.identity(np.shape(A_22)[0])
    B = -(A_22 - (beta * I))
    Q = -A_12
    X = la.solve_sylvester(A, B, Q)
    
    return X
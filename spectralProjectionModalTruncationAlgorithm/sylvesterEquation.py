import numpy as np
import scipy.linalg as la

def solveSylvesterEquation(A, beta, I):
    A = A11 - beta.dot(I)
    B = beta.dot(I) - A22
    Q = -A12
    X = la.solve_sylvester(A, B, Q)
    return X
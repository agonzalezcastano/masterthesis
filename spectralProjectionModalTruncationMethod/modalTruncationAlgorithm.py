import spectralProjection
import blockTriangular
import beta
import sylvesterEquation
import rankRevealingQR
import numpy as np
import scipy.linalg as linalg

def algorithm(A: np.ndarray, B: np.ndarray, C: np.ndarray, D: np.ndarray, inputs: np.ndarray, initial_states: np.ndarray, alpha, reduced_order):
    A = eliminateSmallValuesFromMatrix(A)
    S = spectralProjection.calculateSpectralProjection(A, alpha)
    Q = rankRevealingQR.calculateRankRevealingQ(S)
    Q = nearestPD(Q)

    A_11, A_12, A_21, A_22 = blockTriangular.computeBlockTriangularA(A, Q)
    B_1, B_2 = blockTriangular.computeBlockTriangularB(B, Q)
    C_1, C_2 = blockTriangular.computeBlockTriangularC(C, Q)
    
    beta_param = beta.computeBeta(A, A_11)
    X: np.ndarray = sylvesterEquation.solveSylvesterEquation(A_11, A_12, A_22, beta_param)

    A_r = A_11
    B_r = B_1 - X.dot(B_2)
    C_r = C_1
    D_r = D

    # solve linear system to obtain the reduced states
    #states_r = linalg.solve(-A_r, (0.01-(B_r @ inputs)))
    states_r = linalg.pinv(-A_r) @ (0.01-(B_r @ inputs))
    
    return A_r, B_r, C_r, D_r, states_r

def eliminateSmallValuesFromMatrix(A):
    A= np.tril(A) + np.triu(np.transpose(A), 1)
    A[np.absolute(A) < 0.000001] = 0
    return A

def nearestPD(A):
    B = (A + np.transpose(A)) / 2
    U, s, V = linalg.svd(B)

    H = np.dot(np.transpose(V), (np.diag(s) @ V))

    A2 = (B + H) / 2

    A3 = (A2 + np.transpose(A2)) / 2

    if isPD(A3):
        return A3
    spacing = np.spacing(linalg.norm(A))
    I = np.eye(np.shape(A)[0])
    k = 1
    while not isPD(A3):
        mineig = np.min(np.real(linalg.eigvals(A3)))
        A3 += I * (-mineig * k**2 + spacing)
        k += 1

    return A3

def isPD(B):
    # Returns true when input is positive-definite, via Cholesky
    try:
        _ = linalg.cholesky(B)
        return True
    except linalg.LinAlgError:
        return False

import spectralProjection
import blockTriangular
import beta
import sylvesterEquation
import rankRevealingQR
import numpy as np
import scipy.linalg as linalg

def algorithm(A: np.ndarray, B: np.ndarray, C: np.ndarray, D: np.ndarray, inputs: np.ndarray, initial_states: np.ndarray, alpha, reduced_order):
    P = spectralProjection.calculateSpectralProjection(A, alpha)
    Q = rankRevealingQR.calculateRankRevealingQ(P)

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
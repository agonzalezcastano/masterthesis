import spectralProjection
import blockTriangular
import beta
import sylvesterEquation
import reducedSystem
import rankRevealingQR

import numpy as np

def algorithm(A: np.ndarray, B: np.ndarray, C: np.ndarray, D: np.ndarray, alpha: np.ndarray):
    
    I = np.identity(A.shape[0])

    P = spectralProjection.calculateSpectralProjection(A, I, alpha)
    Q = rankRevealingQR.calculateRankRevealingQ(P)
    A_11, A_12, A_21, A_22 = blockTriangular.computeBlockTriangularA(A, Q)
    B_1, B_2 = blockTriangular.computeBlockTriangularA(B, Q)
    C_1, C_2 = blockTriangular.computeBlockTriangularA(C, Q)
    
    beta_param = beta.computeBeta(A)
    
    X: np.ndarray = sylvesterEquation.solveSylvesterEquation(A, beta_param, I)
    
    A_r = A_11
    B_r = B_1 - X.dot(B_2)
    C_r = C_1
    D_r = D
    
    G_r = reducedSystem.createReducedSystem(A_r, B_r, C_r, D_r)
    
    return G_r
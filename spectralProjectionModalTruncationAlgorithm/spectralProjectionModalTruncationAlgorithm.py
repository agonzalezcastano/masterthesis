import numpy as np
import scipy as sci

def spectralProjectionModalTruncationAlgorithm(A, B, C, D, alpha):
    
    TF = sci.signal.TransferFunction()
    
    I = np.identity(A.shape[0])

    P = calculateSpectralProjection(A, I, alpha)
    Q = calculateRankRevealingQ(P)
    A11, A12, A22 = computeBlockTriangularA(A, Q)
    B1, B2 = computeBlockTriangularA(B, Q)
    C1, C2 = computeBlockTriangularA(C, Q)
    
    beta = computeBeta(A)
    
    X = solveSylvesterEquation(A, beta, I)
    
    Ar = A11
    Br = B1 - X.dot(B2)
    Cr = C1
    Dr = D
    
    Gr = createReducedSystem(Ar, Br, Cr, Dr)
    
    return Gr
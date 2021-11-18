import numpy as np
import scipy.linalg as la

def computeBlockTriangularA(A, Q):
    triA = Q.transpose().dot(A).dot(Q)
    
    heigh = triA.shape[0]
    weight = triA.shape[1]
    heigh_2 = heigh/2
    weight_2 = weight/2
    
    A11 = triA[:heigh_2, :weight_2]
    A12 = triA[(heigh_2 + 1):, :weight_2]
    A22 = triA[(heigh_2 + 1):, (weight_2 + 1):]

    return A11, A12, A22
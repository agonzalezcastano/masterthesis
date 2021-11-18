import numpy as np
import scipy.linalg as la

def computeBlockTriangularC(C, Q):
    triC = C.dot(Q)

    heigh = triC.shape[0]
    weight = triC.shape[1]
    heigh_2 = heigh/2
    weight_2 = weight/2
    
    C1 = triC[:, :weight_2]
    C2 = triC[:, (weight_2 + 1):]

    return C1, C2
import numpy as np
import scipy.linalg as la

def computeBlockTriangularB(B, Q):
    triB = Q.transpose().dot(B)

    heigh = triB.shape[0]
    weight = triB.shape[1]
    heigh_2 = heigh/2
    weight_2 = weight/2
    
    B1 = triB[:, :weight_2]
    B2 = triB[:, (weight_2 + 1):]

    return B1, B2
from numpy import ndarray
import numpy as np

def decomposeMatrixInFour(A: ndarray):
    heigh = A.shape[0]
    weight = A.shape[1]

    if heigh % 2 != 0:
        A = A[:(heigh-1), :(weight-1)]
        heigh = A.shape[0]
        weight = A.shape[1]
    
    heigh_2 = int(heigh/2)
    weight_2 = int(weight/2)

    A_11: ndarray = A[:heigh_2, :weight_2]
    A_12: ndarray = A[heigh_2:, :weight_2]
    A_21: ndarray = A[:heigh_2, weight_2:]
    A_22: ndarray = A[heigh_2:, weight_2:]

    return A_11, A_12, A_21, A_22

def decomposeMatrixInTwo(A: ndarray):
    heigh = A.shape[0]

    if heigh % 2 != 0:
        A = A[:(heigh-1), :]
        heigh = A.shape[0]
    
    heigh_2 = int(heigh/2)
    
    A_1: ndarray = A[:heigh_2, :]
    A_2: ndarray = A[heigh_2:, :]

    return A_1, A_2
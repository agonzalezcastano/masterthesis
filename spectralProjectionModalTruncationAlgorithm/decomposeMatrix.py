from numpy import ndarray

def decomposeMatrixInFour(A: ndarray):

    heigh = A.shape[0]
    weight = A.shape[1]
    heigh_2 = heigh/2
    weight_2 = weight/2
   
    A_11 = A[:heigh_2, :weight_2]
    A_12 = A[(heigh_2 + 1):, :weight_2]
    A_21 = A[:heigh_2, (weight_2 + 1):]
    A_22 = A[(heigh_2 + 1):, (weight_2 + 1):]

    return A_11, A_12, A_21, A_22


def decomposeMatrixInTwo(A: ndarray):

    weight = A.shape[1]
    weight_2 = weight/2
    
    A_1 = A[:, :weight_2]
    A_2 = A[:, (weight_2 + 1):]

    return A_1, A_2
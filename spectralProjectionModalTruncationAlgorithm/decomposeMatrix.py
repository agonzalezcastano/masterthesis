def decomposeMatrixInFour(A):

    heigh = A.shape[0]
    weight = A.shape[1]
    heigh_2 = heigh/2
    weight_2 = weight/2
   
    A11 = A[:heigh_2, :weight_2]
    A12 = A[(heigh_2 + 1):, :weight_2]
    A21 = A[:heigh_2, (weight_2 + 1):]
    A22 = A[(heigh_2 + 1):, (weight_2 + 1):]

    return A11, A12, A21, A22


def decomposeMatrixInTwo(A):

    weight = A.shape[1]
    weight_2 = weight/2
    
    A1 = A[:, :weight_2]
    A2 = A[:, (weight_2 + 1):]

    return A1, A2
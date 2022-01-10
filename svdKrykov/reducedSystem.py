import reducedMatrix

def computeReducedSystem(A, B, C, D, Z, V):
    A_r = reducedMatrix.computeReducedMatrixA(A, Z, V)
    B_r = reducedMatrix.computeReducedMatrixB(B, Z)
    C_r = reducedMatrix.computeReducedMatrixC(C, V)
    D_r = D
    
    return A_r, B_r, C_r, D_r
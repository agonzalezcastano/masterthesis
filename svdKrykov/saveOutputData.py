from systemExamples.transformationsCsv import Csv

def saveDataIntoMatrix(isPartData: bool, A_r, B_r, C_r, D_r, states_r):
    if isPartData:
        Csv.transformMatrixToCVS(A_r, "part_A_svdKrylov")
        Csv.transformMatrixToCVS(B_r, "part_B_svdKrylov")
        Csv.transformMatrixToCVS(C_r, "part_C_svdKrylov")
        Csv.transformMatrixToCVS(D_r, "part_D_svdKrylov")
        Csv.transformMatrixToCVS(states_r, "part_states_svdKrylov")

    else:
        Csv.transformMatrixToCVS(A_r, "A_svdKrylov")
        Csv.transformMatrixToCVS(B_r, "B_svdKrylov")
        Csv.transformMatrixToCVS(C_r, "C_svdKrylov")
        Csv.transformMatrixToCVS(D_r, "D_svdKrylov")
        Csv.transformMatrixToCVS(states_r, "states_svdKrylov")
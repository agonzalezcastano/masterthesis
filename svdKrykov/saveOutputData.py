from systemExamples.transformationsCsv import Csv

def saveIEEE34DataIntoMatrix(isPartData: bool, systemName, A_r, B_r, C_r, D_r, states_r):
    if isPartData:
        Csv.transformMatrixToCVS(A_r, systemName, "part_A_svdKrylov")
        Csv.transformMatrixToCVS(B_r, systemName, "part_B_svdKrylov")
        Csv.transformMatrixToCVS(C_r, systemName, "part_C_svdKrylov")
        Csv.transformMatrixToCVS(D_r, systemName, "part_D_svdKrylov")
        Csv.transformMatrixToCVS(states_r, systemName, "part_states_svdKrylov")

    else:
        Csv.transformMatrixToCVS(A_r, systemName, "A_svdKrylov")
        Csv.transformMatrixToCVS(B_r, systemName, "B_svdKrylov")
        Csv.transformMatrixToCVS(C_r, systemName, "C_svdKrylov")
        Csv.transformMatrixToCVS(D_r, systemName, "D_svdKrylov")
        Csv.transformMatrixToCVS(states_r, systemName, "states_svdKrylov")

def saveDataIntoMatrix(systemName, A_r, B_r, C_r, D_r, states_r):
    Csv.transformMatrixToCVS(A_r, systemName, "A_svdKrylov")
    Csv.transformMatrixToCVS(B_r, systemName, "B_svdKrylov")
    Csv.transformMatrixToCVS(C_r, systemName, "C_svdKrylov")
    Csv.transformMatrixToCVS(D_r, systemName, "D_svdKrylov")
    Csv.transformMatrixToCVS(states_r, systemName, "states_svdKrylov")
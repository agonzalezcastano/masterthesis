from systemExamples.transformationsCsv import Csv

def saveIEEE34DataIntoMatrix(isPartData: bool, systemName, A_r, B_r, C_r, D_r, states_r):
    if isPartData:
        Csv.transformMatrixToCVS(A_r, systemName, "part_A_spectralProjection")
        Csv.transformMatrixToCVS(B_r, systemName, "part_B_spectralProjection")
        Csv.transformMatrixToCVS(C_r, systemName, "part_C_spectralProjection")
        Csv.transformMatrixToCVS(D_r, systemName, "part_D_spectralProjection")
        Csv.transformMatrixToCVS(states_r, systemName, "part_states_spectralProjection")

    else:
        Csv.transformMatrixToCVS(A_r, systemName, "A_spectralProjection")
        Csv.transformMatrixToCVS(B_r, systemName, "B_spectralProjection")
        Csv.transformMatrixToCVS(C_r, systemName, "C_spectralProjection")
        Csv.transformMatrixToCVS(D_r, systemName, "D_spectralProjection")
        Csv.transformMatrixToCVS(states_r, systemName, "states_spectralProjection")

def saveDataIntoMatrix(systemName, A_r, B_r, C_r, D_r, states_r):
    Csv.transformMatrixToCVS(A_r, systemName, "A_spectralProjection")
    Csv.transformMatrixToCVS(B_r, systemName, "B_spectralProjection")
    Csv.transformMatrixToCVS(C_r, systemName, "C_spectralProjection")
    Csv.transformMatrixToCVS(D_r, systemName, "D_spectralProjection")
    Csv.transformMatrixToCVS(states_r, systemName, "states_spectralProjection")
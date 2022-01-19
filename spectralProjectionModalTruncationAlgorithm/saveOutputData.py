from systemExamples.transformationsCsv import Csv

def saveDataIntoMatrix(isPartData: bool, A_r, B_r, C_r, D_r, states_r):
    if isPartData:
        Csv.transformMatrixToCVS(A_r, "part_A_spectralProjection")
        Csv.transformMatrixToCVS(B_r, "part_B_spectralProjection")
        Csv.transformMatrixToCVS(C_r, "part_C_spectralProjection")
        Csv.transformMatrixToCVS(D_r, "part_D_spectralProjection")
        Csv.transformMatrixToCVS(states_r, "part_states_spectralProjection")

    else:
        Csv.transformMatrixToCVS(A_r, "A_spectralProjection")
        Csv.transformMatrixToCVS(B_r, "B_spectralProjection")
        Csv.transformMatrixToCVS(C_r, "C_spectralProjection")
        Csv.transformMatrixToCVS(D_r, "D_spectralProjection")
        Csv.transformMatrixToCVS(states_r, "states_spectralProjection")
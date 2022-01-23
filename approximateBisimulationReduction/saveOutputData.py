from systemExamples.transformationsCsv import Csv

def saveIEEE34DataIntoMatrix(isPartData: bool, systemName, A_r, B_r, C_r, D_r, states_r):
    if isPartData:
        Csv.transformMatrixToCVS(A_r, systemName, "part_A_approximateBisimulation")
        Csv.transformMatrixToCVS(B_r, systemName, "part_B_approximateBisimulation")
        Csv.transformMatrixToCVS(C_r, systemName, "part_C_approximateBisimulation")
        Csv.transformMatrixToCVS(D_r, systemName, "part_D_approximateBisimulation")
        Csv.transformMatrixToCVS(states_r, systemName, "part_states_approximateBisimulation")

    else:
        Csv.transformMatrixToCVS(A_r, systemName, "A_approximateBisimulation")
        Csv.transformMatrixToCVS(B_r, systemName, "B_approximateBisimulation")
        Csv.transformMatrixToCVS(C_r, systemName, "C_approximateBisimulation")
        Csv.transformMatrixToCVS(D_r, systemName, "D_approximateBisimulation")
        Csv.transformMatrixToCVS(states_r, systemName, "states_approximateBisimulation")

def saveDataIntoMatrix(systemName, A_r, B_r, C_r, D_r, states_r):
    Csv.transformMatrixToCVS(A_r, systemName, "A_approximateBisimulation")
    Csv.transformMatrixToCVS(B_r, systemName, "B_approximateBisimulation")
    Csv.transformMatrixToCVS(C_r, systemName, "C_approximateBisimulation")
    Csv.transformMatrixToCVS(D_r, systemName, "D_approximateBisimulation")
    Csv.transformMatrixToCVS(states_r, systemName, "states_approximateBisimulation")
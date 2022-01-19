from systemExamples.transformationsCsv import Csv

def saveDataIntoMatrix(isPartData: bool, A_r, B_r, C_r, D_r, states_r):
        if isPartData:
            Csv.transformMatrixToCVS(A_r, "part_A_approximateBisimulation")
            Csv.transformMatrixToCVS(B_r, "part_B_approximateBisimulation")
            Csv.transformMatrixToCVS(C_r, "part_C_approximateBisimulation")
            Csv.transformMatrixToCVS(D_r, "part_D_approximateBisimulation")
            Csv.transformMatrixToCVS(states_r, "part_states_approximateBisimulation")

        else:
            Csv.transformMatrixToCVS(A_r, "A_approximateBisimulation")
            Csv.transformMatrixToCVS(B_r, "B_approximateBisimulation")
            Csv.transformMatrixToCVS(C_r, "C_approximateBisimulation")
            Csv.transformMatrixToCVS(D_r, "D_approximateBisimulation")
            Csv.transformMatrixToCVS(states_r, "states_approximateBisimulation")
from numpy import imag
from systemExamples.transformationsCsv import Csv

def saveDataIntoMatrix(systemName, A_r, B_r, C_r, D_r, states_r, output):
    Csv.transformMatrixToCVS(A_r, systemName, "A_approximateBisimulation")
    Csv.transformMatrixToCVS(B_r, systemName, "B_approximateBisimulation")
    Csv.transformMatrixToCVS(C_r, systemName, "C_approximateBisimulation")
    Csv.transformMatrixToCVS(D_r, systemName, "D_approximateBisimulation")
    Csv.transformMatrixToCVS(states_r, systemName, "states_approximateBisimulation")
    initial_states_r = imag(states_r)
    Csv.transformComplexMatrixToCVS(initial_states_r, systemName, "initial_states_approximateBisimulation")
    Csv.transformMatrixToCVS(output, systemName, "output_approximateBisimulation")
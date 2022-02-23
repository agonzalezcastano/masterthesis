from numpy import imag
from systemExamples.transformationsCsv import Csv

def saveDataIntoMatrix(systemName, A_r, B_r, C_r, D_r, states_r, output):
    Csv.transformMatrixToCVS(A_r, systemName, "A_svdKrylov")
    Csv.transformMatrixToCVS(B_r, systemName, "B_svdKrylov")
    Csv.transformMatrixToCVS(C_r, systemName, "C_svdKrylov")
    Csv.transformMatrixToCVS(D_r, systemName, "D_svdKrylov")
    Csv.transformMatrixToCVS(states_r, systemName, "states_svdKrylov")
    initial_states_r = imag(states_r)
    Csv.transformComplexMatrixToCVS(initial_states_r, systemName, "initial_states_svdKrylov")
    Csv.transformMatrixToCVS(output, systemName, "output_svdKrylov")
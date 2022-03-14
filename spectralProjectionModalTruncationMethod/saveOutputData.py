from numpy import imag
from systemExamples.transformationsCsv import Csv

def saveDataIntoMatrix(systemName, A_r, B_r, C_r, D_r, states_r, output):
    Csv.transformMatrixToCVS(A_r, systemName, "A_spectralProjection")
    Csv.transformMatrixToCVS(B_r, systemName, "B_spectralProjection")
    Csv.transformMatrixToCVS(C_r, systemName, "C_spectralProjection")
    Csv.transformMatrixToCVS(D_r, systemName, "D_spectralProjection")
    Csv.transformComplexMatrixToCVS(states_r, systemName, "states_spectralProjection")
    initial_states_r = imag(states_r)
    Csv.transformComplexMatrixToCVS(initial_states_r, systemName, "initial_states_spectralProjection")
    Csv.transformComplexMatrixToCVS(output, systemName, "output_spectralProjection")
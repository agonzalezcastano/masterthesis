import csv
import numpy as np

class Csv:
    def transformCsvToMatrix(csvFile: csv):
        numpy_array = np.loadtxt(open("../systemExamples/data/" + csvFile + ".csv"), delimiter=",", dtype = "float")

        rows = np.shape(numpy_array)[0]
        cols = np.shape(numpy_array)[1]
        result = np.ndarray((rows, cols), dtype = "float")

        for x in range(0, cols - 1):
            for y in range(0, rows - 1):
                result[y][x] = float(numpy_array[y,x])

        return result
    
    def transformComplexCsvToMatrix(csvFile: csv):
        numpy_array = np.loadtxt(open("../systemExamples/data/" + csvFile + ".csv"), delimiter=",", dtype = "str")

        rows = np.shape(numpy_array)[0]
        result = np.ndarray((rows, 1), dtype = "complex")

        for x in range(0, rows - 1):
            numpy_array[x] = numpy_array[x].replace('i', 'j')
            result[x] = complex(numpy_array[x])

        return result
    
    def transformMatrixToCVS(A: np.ndarray, matrixName):
        np.savetxt("../results/ieee34_reduced_" + matrixName + ".csv", A, fmt="%f", delimiter=",")


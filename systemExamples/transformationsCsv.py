import csv
import numpy

class Csv:
    def transformCsvToMatrix(csvFile: csv):
        reader = csv.reader(open("../systemExamples/data/" + csvFile + ".csv"), delimiter=",")
        x = list(reader)
        result = numpy.array(x).astype("float")
        return result
    
    def transformMatrixToCVS(A: numpy.ndarray, matrixName):
        numpy.savetxt("../results/ieee34_reduced_" + matrixName + ".csv", A, fmt="%d", delimiter=",") 

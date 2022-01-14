import numpy as np
import csv
from systemExamples.transformationsCsv import Csv

def cleanAndFixTypeDataVector(csvFile: csv):
    numpy_array = np.loadtxt(open("../results/" + csvFile + ".csv"), delimiter=",", dtype = "str")
    rows = np.shape(numpy_array)[0]
    result = np.ndarray((rows, 1), dtype = "complex")

    for x in range(0, rows - 1):
        numpy_array[x] = numpy_array[x].replace('(', '')
        numpy_array[x] = numpy_array[x].replace(')', '')
        result[x] = complex(numpy_array[x])

    np.savetxt("../results/" + csvFile + ".csv", result, fmt="%f", delimiter=",")

def cleanAndFixTypeDataMatrix(csvFile: csv):
    numpy_array = np.loadtxt(open("../results/" + csvFile + ".csv"), delimiter=",", dtype = "str")

    rows = np.shape(numpy_array)[0]
    cols = np.shape(numpy_array)[1]
    result = np.ndarray((rows, cols), dtype = "complex")

    for x in range(0, cols - 1):
        for y in range(0, rows - 1):
            numpy_array[y][x] = numpy_array[y][x].replace('(', '')
            numpy_array[y][x] = numpy_array[y][x].replace(')', '')
            result[y][x] = complex(numpy_array[y,x])

    np.savetxt("../results/" + csvFile + ".csv", result, fmt="%f", delimiter=",")

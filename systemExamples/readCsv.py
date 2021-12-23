import csv
import numpy

def transformCsvToMatrix(csvFile: csv):
    reader = csv.reader(open("systemExamples/data/" + csvFile + ".csv"), delimiter=",")
    x = list(reader)
    result = numpy.array(x).astype("float")
    return result
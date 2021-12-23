import sys
sys.path.append('../')
from systemExamples.transformationsCsv import Csv

class SystemExample:
    def setPartDataIEEE34SystemExample():
        A = Csv.transformCsvToMatrix('ieee34_part_data_A')
        B = Csv.transformCsvToMatrix('ieee34_part_data_B')
        C = Csv.transformCsvToMatrix('ieee34_part_data_C')
        D = Csv.transformCsvToMatrix('ieee34_part_data_D')

        return A, B, C, D
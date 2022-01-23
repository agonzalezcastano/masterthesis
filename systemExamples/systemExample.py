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
    
    def setDataIEEE34SystemExample():
        A = Csv.transformCsvToMatrix('ieee34_data_A')
        B = Csv.transformCsvToMatrix('ieee34_data_B')
        C = Csv.transformCsvToMatrix('ieee34_data_C')
        D = Csv.transformCsvToMatrix('ieee34_data_D')

        return A, B, C, D

    def setDataIEEE123SystemExample():
        A = Csv.transformCsvToMatrix('ieee123_data_A')
        B = Csv.transformCsvToMatrix('ieee123_data_B')
        C = Csv.transformCsvToMatrix('ieee123_data_C')
        D = Csv.transformCsvToMatrix('ieee123_data_D')

        return A, B, C, D
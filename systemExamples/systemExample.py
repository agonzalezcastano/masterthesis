import readCsv

def setPartDataIEEE34SystemExample():
    A = readCsv.transformCsvToMatrix('ieee34_part_data_A')
    B = readCsv.transformCsvToMatrix('ieee34_part_data_B')
    C = readCsv.transformCsvToMatrix('ieee34_part_data_C')
    D = readCsv.transformCsvToMatrix('ieee34_part_data_D')

    return A, B, C, D

A, B, C, D = setPartDataIEEE34SystemExample()

print(A)
import sys
sys.path.append('../')
from systemExamples.transformationsCsv import Csv

class SystemExample:
    def setDataIEEE34SystemExample():
        A = Csv.transformCsvToMatrix('ieee34_data_A')
        B = Csv.transformCsvToMatrix('ieee34_data_B')
        C = Csv.transformCsvToMatrix('ieee34_data_C')
        D = Csv.transformCsvToMatrix('ieee34_data_D')
        inputs = Csv.transformComplexCsvToMatrix('ieee34_data_inputs')
        initial_states = Csv.transformComplexCsvToMatrix('ieee34_data_initial_states')
        output = Csv.transformComplexCsvToMatrix('ieee34_data_output')

        return A, B, C, D, inputs, initial_states, output
    
    def setDataIEEE18SystemExample():
        A = Csv.transformCsvToMatrix('ieee18_data_A')
        B = Csv.transformCsvToMatrix('ieee18_data_B')
        C = Csv.transformCsvToMatrix('ieee18_data_C')
        D = Csv.transformCsvToMatrix('ieee18_data_D')
        inputs = Csv.transformComplexCsvToMatrix('ieee18_data_inputs')
        initial_states = Csv.transformComplexCsvToMatrix('ieee18_data_initial_states')
        output = Csv.transformComplexCsvToMatrix('ieee18_data_output')

        return A, B, C, D, inputs, initial_states, output

    def setDataIEEE7SystemExample():
        A = Csv.transformCsvToMatrix('ieee7_data_A')
        B = Csv.transformCsvToMatrix('ieee7_data_B')
        C = Csv.transformCsvToMatrix('ieee7_data_C')
        D = Csv.transformCsvToMatrix('ieee7_data_D')
        inputs = Csv.transformComplexCsvToMatrix('ieee7_data_inputs')
        initial_states = Csv.transformComplexCsvToMatrix('ieee7_data_initial_states')
        output = Csv.transformComplexCsvToMatrix('ieee7_data_output')

        return A, B, C, D, inputs, initial_states, output
    
    def setDataIEEE5SystemExample():
        A = Csv.transformCsvToMatrix('ieee5_data_A')
        B = Csv.transformCsvToMatrix('ieee5_data_B')
        C = Csv.transformCsvToMatrix('ieee5_data_C')
        D = Csv.transformCsvToMatrix('ieee5_data_D')
        inputs = Csv.transformComplexCsvToMatrix('ieee5_data_inputs')
        initial_states = Csv.transformComplexCsvToMatrix('ieee5_data_initial_states')
        output = Csv.transformComplexCsvToMatrix('ieee5_data_output')

        return A, B, C, D, inputs, initial_states, output
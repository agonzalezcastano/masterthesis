import sys
sys.path.append('../')
from systemExamples.transformationsCsv import Csv

class SystemExample:
    def setContinuousDataIEEE34SystemExample():
        A = Csv.transformCsvToMatrix('continuous/ieee34_data_A')
        B = Csv.transformCsvToMatrix('continuous/ieee34_data_B')
        C = Csv.transformCsvToMatrix('continuous/ieee34_data_C')
        D = Csv.transformCsvToMatrix('continuous/ieee34_data_D')
        inputs = Csv.transformComplexCsvToMatrix('continuous/ieee34_data_inputs')
        initial_states = Csv.transformComplexCsvToMatrix('continuous/ieee34_data_initial_states')
        output = Csv.transformComplexCsvToMatrix('continuous/ieee34_data_output')

        return A, B, C, D, inputs, initial_states, output
    
    def setContinuousDataIEEE18SystemExample():
        A = Csv.transformCsvToMatrix('continuous/ieee18_data_A')
        B = Csv.transformCsvToMatrix('continuous/ieee18_data_B')
        C = Csv.transformCsvToMatrix('continuous/ieee18_data_C')
        D = Csv.transformCsvToMatrix('continuous/ieee18_data_D')
        inputs = Csv.transformComplexCsvToMatrix('continuous/ieee18_data_inputs')
        initial_states = Csv.transformComplexCsvToMatrix('continuous/ieee18_data_initial_states')
        output = Csv.transformComplexCsvToMatrix('continuous/ieee18_data_output')

        return A, B, C, D, inputs, initial_states, output

    def setContinuousDataIEEE7SystemExample():
        A = Csv.transformCsvToMatrix('continuous/ieee7_data_A')
        B = Csv.transformCsvToMatrix('continuous/ieee7_data_B')
        C = Csv.transformCsvToMatrix('continuous/ieee7_data_C')
        D = Csv.transformCsvToMatrix('continuous/ieee7_data_D')
        inputs = Csv.transformComplexCsvToMatrix('continuous/ieee7_data_inputs')
        initial_states = Csv.transformComplexCsvToMatrix('continuous/ieee7_data_initial_states')
        output = Csv.transformComplexCsvToMatrix('continuous/ieee7_data_output')

        return A, B, C, D, inputs, initial_states, output
    
    def setContinuousDataIEEE5SystemExample():
        A = Csv.transformCsvToMatrix('continuous/ieee5_data_A')
        B = Csv.transformCsvToMatrix('continuous/ieee5_data_B')
        C = Csv.transformCsvToMatrix('continuous/ieee5_data_C')
        D = Csv.transformCsvToMatrix('continuous/ieee5_data_D')
        inputs = Csv.transformComplexCsvToMatrix('continuous/ieee5_data_inputs')
        initial_states = Csv.transformComplexCsvToMatrix('continuous/ieee5_data_initial_states')
        output = Csv.transformComplexCsvToMatrix('continuous/ieee5_data_output')

        return A, B, C, D, inputs, initial_states, output

    def setDiscreteDataIEEE34SystemExample():
        A = Csv.transformCsvToMatrix('discrete/ieee34_data_A')
        B = Csv.transformCsvToMatrix('discrete/ieee34_data_B')
        C = Csv.transformCsvToMatrix('discrete/ieee34_data_C')
        D = Csv.transformCsvToMatrix('discrete/ieee34_data_D')
        inputs = Csv.transformComplexCsvToMatrix('discrete/ieee34_data_inputs')
        initial_states = Csv.transformComplexCsvToMatrix('discrete/ieee34_data_initial_states')
        output = Csv.transformComplexCsvToMatrix('discrete/ieee34_data_output')

        return A, B, C, D, inputs, initial_states, output
    
    def setDiscreteDataIEEE18SystemExample():
        A = Csv.transformCsvToMatrix('discrete/ieee18_data_A')
        B = Csv.transformCsvToMatrix('discrete/ieee18_data_B')
        C = Csv.transformCsvToMatrix('discrete/ieee18_data_C')
        D = Csv.transformCsvToMatrix('discrete/ieee18_data_D')
        inputs = Csv.transformComplexCsvToMatrix('discrete/ieee18_data_inputs')
        initial_states = Csv.transformComplexCsvToMatrix('discrete/ieee18_data_initial_states')
        output = Csv.transformComplexCsvToMatrix('discrete/ieee18_data_output')

        return A, B, C, D, inputs, initial_states, output

    def setDiscreteDataIEEE7SystemExample():
        A = Csv.transformCsvToMatrix('discrete/ieee7_data_A')
        B = Csv.transformCsvToMatrix('discrete/ieee7_data_B')
        C = Csv.transformCsvToMatrix('discrete/ieee7_data_C')
        D = Csv.transformCsvToMatrix('discrete/ieee7_data_D')
        inputs = Csv.transformComplexCsvToMatrix('discrete/ieee7_data_inputs')
        initial_states = Csv.transformComplexCsvToMatrix('discrete/ieee7_data_initial_states')
        output = Csv.transformComplexCsvToMatrix('discrete/ieee7_data_output')

        return A, B, C, D, inputs, initial_states, output
    
    def setDiscreteDataIEEE5SystemExample():
        A = Csv.transformCsvToMatrix('discrete/ieee5_data_A')
        B = Csv.transformCsvToMatrix('discrete/ieee5_data_B')
        C = Csv.transformCsvToMatrix('discrete/ieee5_data_C')
        D = Csv.transformCsvToMatrix('discrete/ieee5_data_D')
        inputs = Csv.transformComplexCsvToMatrix('discrete/ieee5_data_inputs')
        initial_states = Csv.transformComplexCsvToMatrix('discrete/ieee5_data_initial_states')
        output = Csv.transformComplexCsvToMatrix('discrete/ieee5_data_output')

        return A, B, C, D, inputs, initial_states, output
import sys
from svdKrykov.saveOutputData import saveIEEE34DataIntoMatrix
sys.path.append('../')
from systemExamples.systemExample import SystemExample
from systemExamples.transformationsCsv import Csv
import interactiveSvdKrylov
from timeit import default_timer as timer
import numpy as np
from saveOutputData import saveDataIntoMatrix
import results.calculateError as calculateError

class Menu:
    def __init__(self):
        self.loop = True
        self.interpolation_points = 0
        self.error_tolerance = 0.1
        self.reduced_order = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.inputs = 0
        self.initial_states = 0
        self.output = 0
        self.start_time = 0
        self.isPartData = False
        self.isIEEE34 = False


    def switch(self, option_number):
        default = "Invalid input. Please enter a number between 1 and 5 or exit."
        return getattr(self, "option_" + str(option_number), lambda: default)()

    def print_menu(self):
        print(20 * "-", "SVD-Krylov Algorithm's Menu", 20 * "-")
        print("1. Set the reduced-order to be achieved (k)")
        print("2. Set the error tolerance (e)")
        print("3. Set the IEEE 34 partial data system")
        print("4. Set the IEEE 34 system")
        print("5. Set the IEEE 123 system")
        print("6. Execute Interactive SVD-Krylov reduction algorithm")
        print("e. Exit")
        print(67 * "-")
        option_choice = input("Enter an option [1-6/e]: ")
        print("Option " + option_choice + " chosen")
        return option_choice

    def option_1(self):
        self.reduced_order = input("Enter the value for the reduced-order you wish to obtain (k): ")
        self.reduced_order = int(self.reduced_order)

    def option_2(self):
        self.error_tolerance = input("Enter the value for the error tolerance (e): ")
        self.error_tolerance = float(self.error_tolerance)

    def option_3(self):
        self.A, self.B, self.C, self.D = SystemExample.setPartDataIEEE34SystemExample()
        self.inputs = Csv.transformComplexCsvToMatrix('ieee34_part_data_inputs')
        self.initial_states = Csv.transformComplexCsvToMatrix('ieee34_part_data_initial_states')
        self.output = Csv.transformComplexCsvToMatrix('ieee34_part_data_output')
        self.interpolation_points = int(self.reduced_order/np.shape(self.B)[1])
        self.isPartData = True
        self.isIEEE34 = True

    def option_4(self):
        self.A, self.B, self.C, self.D = SystemExample.setDataIEEE34SystemExample()
        self.inputs = Csv.transformComplexCsvToMatrix('ieee34_data_inputs')
        self.initial_states = Csv.transformComplexCsvToMatrix('ieee34_data_initial_states')
        self.output = Csv.transformComplexCsvToMatrix('ieee34_data_output')
        self.interpolation_points = int(self.reduced_order/np.shape(self.B)[1])
        self.isPartData = False
        self.isIEEE34 = True

    def option_5(self):
        self.A, self.B, self.C, self.D = SystemExample.setDataIEEE123SystemExample()
        self.inputs = Csv.transformComplexCsvToMatrix('ieee123_data_inputs')
        self.initial_states = Csv.transformComplexCsvToMatrix('ieee123_data_initial_states')
        self.output = Csv.transformComplexCsvToMatrix('ieee123_data_output')
        self.interpolation_points = int(self.reduced_order/np.shape(self.B)[1])
        self.isIEEE34 = True

    def option_6(self):
        start = timer()
        A_r, B_r, C_r, D_r, states_r = interactiveSvdKrylov.algorithm(
            self.A, self.B, self.C, self.D, self.inputs, self.interpolation_points, self.error_tolerance)
        self.reduced_order = np.shape(A_r)[0]
        print("Execution time: %s seconds" % (timer() - start))
        print("Reduced order: %i" % self.reduced_order)

        output = np.dot(C_r, states_r) - np.dot(D_r, self.inputs)
        steady_state_error = calculateError.steady_state_error(self.output, output)
        print("Steady-state error vector: ")
        print(steady_state_error)

        if self.isIEEE34:
            calculateError.print_relative_error_IEEE34_bus_800(self.output, output)
            calculateError.print_relative_error_IEEE34_bus_812(self.output, output)
            calculateError.print_relative_error_IEEE34_bus_830(self.output, output)
            calculateError.print_relative_error_IEEE34_bus_836(self.output, output)
            calculateError.print_relative_error_IEEE34_bus_846(self.output, output)
            saveIEEE34DataIntoMatrix(self.isPartData, "ieee34", A_r, B_r, C_r, D_r, states_r)
        else:
            calculateError.print_relative_error_IEEE123_bus_30(self.output, output)
            calculateError.print_relative_error_IEEE123_bus_60(self.output, output)
            calculateError.print_relative_error_IEEE123_bus_83(self.output, output)
            calculateError.print_relative_error_IEEE123_bus_95(self.output, output)
            calculateError.print_relative_error_IEEE123_bus_151(self.output, output)
            saveDataIntoMatrix("ieee123", A_r, B_r, C_r, D_r, states_r)

    def option_e(self):
        print("Bye!")
        self.loop = False

if __name__ == "__main__":
    main_menu = Menu()
    while main_menu.loop:
        menu_choice = main_menu.print_menu()
        if menu_choice:
            main_menu.switch(menu_choice)
        else:
            menu_choice = input("Wrong option. Enter any key to try again... ")
            main_menu.switch(menu_choice)
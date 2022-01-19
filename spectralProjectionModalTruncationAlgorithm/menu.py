import sys
sys.path.append('../')
from systemExamples.systemExample import SystemExample
from systemExamples.transformationsCsv import Csv
import modalTruncationAlgorithm
import numpy as np
from timeit import default_timer as timer
from saveOutputData import saveDataIntoMatrix
import results.calculateError as calculateError

class Menu:
    def __init__(self):
        self.loop = True
        self.alpha = 1
        self.error_tolerance = 0.1
        self.reduced_order = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.start_time = 0
        self.inputs = 0
        self.initial_states = 0
        self.output = 0
        self.isPartData = False


    def switch(self, option_number):
        default = "Invalid input. Please enter a number between 1 and 6 or exit."
        return getattr(self, "option_" + str(option_number), lambda: default)()

    def print_menu(self):
        print(7 * "-", "Spectral Projection Modal Truncation Algorithm's Menu", 7 * "-")
        print("1. Set the stability margin (alpha)")
        print("2. Set the error tolerance (e)")
        print("3. Set the minimun reduced order (k)")
        print("4. Set the IEEE34 partial data system")
        print("5. Set the IEEE34 system")
        print("6. Execute Spectral Projection Modal Truncation reduction algorithm")
        print("e. Exit")
        print(69 * "-")
        option_choice = input("Enter an option [1-6/e]: ")
        print("Option " + option_choice + " chosen")
        return option_choice

    def option_1(self):
        self.alpha = input("Enter the value for the stability margin (alpha): ")
        self.alpha = float(self.alpha)

    def option_2(self):
        self.error_tolerance = input("Enter the value for the error tolerance (e): ")
        self.error_tolerance = float(self.error_tolerance)

    def option_3(self):
        self.reduced_order = input("Enter the value for reduced-order you wish to obtain (k): ")
        self.reduced_order = int(self.reduced_order)

    def option_4(self):
        self.A, self.B, self.C, self.D = SystemExample.setPartDataIEEE34SystemExample()
        self.inputs = Csv.transformComplexCsvToMatrix('ieee34_part_data_inputs')
        self.initial_states = Csv.transformComplexCsvToMatrix('ieee34_part_data_initial_states')
        self.output = Csv.transformComplexCsvToMatrix('ieee34_part_data_output')
        self.isPartData = True

    def option_5(self):
        self.A, self.B, self.C, self.D = SystemExample.setDataIEEE34SystemExample()
        self.inputs = Csv.transformComplexCsvToMatrix('ieee34_data_inputs')
        self.initial_states = Csv.transformComplexCsvToMatrix('ieee34_data_initial_states')
        self.output = Csv.transformComplexCsvToMatrix('ieee34_data_output')
        self.isPartData = False

    def option_6(self):
        start1 = timer()
        order = np.shape(self.A)[0]
        A_r = self.A
        B_r = self.B
        C_r = self.C
        D_r = self.D

        while order > self.reduced_order:
            start = timer()
            A_r, B_r, C_r, D_r, states_r = modalTruncationAlgorithm.algorithm(A_r, B_r, C_r, D_r, self.alpha, self.inputs)
            order = np.shape(A_r)[0]
            print("Order: ")
            print(order)
            print("Execution time per algorithm execution: %f seconds" % (timer() - start))
    
        end = timer()
        print("Final execution time: %f seconds" % (end - start1))
        print("Reduced order: %i" % order)
        calculateError.steady_state_error(self.output, self.inputs, C_r, D_r, states_r)
        saveDataIntoMatrix(self.isPartData, A_r, B_r, C_r, D_r, states_r)

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
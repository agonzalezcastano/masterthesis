from math import pi
import sys

sys.path.append('../')
from systemExamples.systemExample import SystemExample
from systemExamples.transformationsCsv import Csv
import approximateBisimulation
import time

class Menu:
    def __init__(self):
        self.loop = True
        self.reduced_order = 15
        self.x_max = 0.1
        self.delta_max = pi/2
        self.error_tolerance = 0.1
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.inputs = 0
        self.initial_states = 0
        self.start_time = 0
        self.isPartData = False


    def switch(self, option_number):
        default = "Invalid input. Please enter a number between 1 and 7 or exit."
        return getattr(self, "option_" + str(option_number), lambda: default)()

    def print_menu(self):
        print(30 * "-", "MENU", 30 * "-")
        print("1. Set the reduced-order to be achieved (k)")
        print("2. Set the error tolerance (e)")
        print("3. Set the accuray level (x max)")
        print("4. Set the maximun difference between two rotor angles (delta max)")
        print("5. Set the IEEE34 partial data system")
        print("6. Set the IEEE34 system")
        print("7. Execute Approximate Bisimulation Reduction algorithm")
        print("e. Exit")
        print(67 * "-")
        option_choice = input("Enter an option [1-7/e]: ")
        print("Option " + option_choice + " chosen")
        return option_choice

    def option_1(self):
        self.reduced_order = input("Enter the value for the reduced-order (k): ")

    def option_2(self):
        self.error_tolerance = input("Enter the value for the error tolerance (e): ")

    def option_3(self):
        self.x_max = input("Enter the value for the accuray level (x max): ")

    def option_4(self):
        self.delta_max = input("Enter the value for the maximun difference between two rotor angles (delta max): ")

    def option_5(self):
        self.A, self.B, self.C, self.D = SystemExample.setPartDataIEEE34SystemExample()
        self.inputs = Csv.transformComplexCsvToMatrix('ieee34_part_data_inputs')
        self.initial_states = Csv.transformComplexCsvToMatrix('ieee34_part_data_initial_states')
        self.reduced_order = 15
        self.isPartData = True

    def option_6(self):
        self.A, self.B, self.C, self.D = SystemExample.setDataIEEE34SystemExample()
        self.inputs = Csv.transformComplexCsvToMatrix('ieee34_data_inputs')
        self.initial_states = Csv.transformComplexCsvToMatrix('ieee34_data_initial_states')
        self.reduced_order = 50
        self.isPartData = False

    def option_7(self):
        self.start_time = time.time()
        A_r, B_r, C_r, D_r, inputs_r, states_r = approximateBisimulation.algorithm(
            self.A, self.B, self.C, self.D, self.inputs, self.initial_states, self.reduced_order, self.x_max, self.delta_max, self.error_tolerance)
        print("Execution time: %s seconds" % (time.time() - self.start_time))
        print("Reduced order: %i" % self.reduced_order)

        if self.isPartData:
            Csv.transformMatrixToCVS(A_r, "part_A_approximateBisimulation")
            Csv.transformMatrixToCVS(B_r, "part_B_approximateBisimulation")
            Csv.transformMatrixToCVS(C_r, "part_C_approximateBisimulation")
            Csv.transformMatrixToCVS(D_r, "part_D_approximateBisimulation")
            Csv.transformMatrixToCVS(states_r, "part_states_approximateBisimulation")
            Csv.transformMatrixToCVS(inputs_r, "part_inputs_approximateBisimulation")

        else:
            Csv.transformMatrixToCVS(A_r, "A_approximateBisimulation")
            Csv.transformMatrixToCVS(B_r, "B_approximateBisimulation")
            Csv.transformMatrixToCVS(C_r, "C_approximateBisimulation")
            Csv.transformMatrixToCVS(D_r, "D_approximateBisimulation")
            Csv.transformMatrixToCVS(states_r, "states_approximateBisimulation")
            Csv.transformMatrixToCVS(inputs_r, "inputs_approximateBisimulation")

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
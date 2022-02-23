import cmath
import sys
sys.path.append('../')
from systemExamples.systemExample import SystemExample
from systemExamples.transformationsCsv import Csv
import approximateBisimulation
from timeit import default_timer as timer
from saveOutputData import saveDataIntoMatrix
from saveOutputData import saveIEEE34DataIntoMatrix
import results.calculateError as calculateError
import numpy as np

class Menu:
    def __init__(self):
        self.loop = True
        self.reduced_order = 0
        self.x_max = 10000
        self.delta_max = 10000
        self.error_tolerance = 0.001
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.inputs = 0
        self.initial_states = 0
        self.start_time = 0
        self.isPartData = False
        self.isIEEE34 = False
        self.option_choice = 0


    def switch(self, option_number):
        default = "Invalid input. Please enter a number between 1 and 7 or exit."
        return getattr(self, "option_" + str(option_number), lambda: default)()

    def print_menu(self):
        print(10 * "-", "Approximate Bisimulation Reduction Algorithm's Menu", 10 * "-")
        print("1. Set the reduced-order to be achieved (k)")
        print("2. Set the error tolerance (e)")
        print("3. Set the accuray level (x max)")
        print("4. Set the maximun difference between two outputs (delta max)")
        print("5. Set the IEEE 34 system")
        print("6. Set the IEEE 18 system")
        print("7. Set the IEEE 7 system")
        print("8. Set the IEEE 5 system")
        print("9. Execute Approximate Bisimulation Reduction algorithm")
        print("e. Exit")
        print(71 * "-")
        option_choice = input("Enter an option [1-9/e]: ")
        print("Option " + option_choice + " chosen")
        self.option_choice = option_choice
        return option_choice

    def option_1(self):
        self.reduced_order = input("Enter the value for the reduced-order (k): ")
        self.reduced_order = int(self.reduced_order)

    def option_2(self):
        self.error_tolerance = input("Enter the value for the error tolerance (e): ")
        self.error_tolerance = float(self.error_tolerance)

    def option_3(self):
        self.x_max = input("Enter the value for the accuray level (x max): ")
        self.x_max = float(self.x_max)

    def option_4(self):
        self.delta_max = input("Enter the value for the maximun difference between two rotor angles (delta max): ")
        self.delta_max = float(self.delta_max)

    def option_5(self):
        self.A, self.B, self.C, self.D, self.inputs, self.initial_states, self.output = SystemExample.setDataIEEE34SystemExample()
        self.isPartData = True
        self.isIEEE34 = True

    def option_6(self):
        self.A, self.B, self.C, self.D, self.inputs, self.initial_states, self.output = SystemExample.setDataIEEE18SystemExample()
        self.isPartData = False
        self.isIEEE34 = True
    
    def option_7(self):
        self.A, self.B, self.C, self.D, self.inputs, self.initial_states, self.output = SystemExample.setDataIEEE7SystemExample()
        self.isIEEE34 = False

    def option_8(self):
        self.A, self.B, self.C, self.D, self.inputs, self.initial_states, self.output = SystemExample.setDataIEEE5SystemExample()
        self.isIEEE34 = False

    def option_9(self):
        start = timer()
        A_r, B_r, C_r, D_r, states_r, reduced_order = approximateBisimulation.algorithm(
            self.A, self.B, self.C, self.D, self.inputs, self.output, self.initial_states, self.reduced_order, self.x_max, self.delta_max, self.error_tolerance)
        print("Execution time: %s seconds" % (timer() - start))
        print("Reduced order: %i" % reduced_order)

        output = np.dot(C_r, states_r) + np.dot(D_r, self.inputs)
        
        if self.option_choice == 5:
            saveDataIntoMatrix("ieee34", A_r, B_r, C_r, D_r, states_r, output)
        if self.option_choice == 6:
            saveDataIntoMatrix("ieee18", A_r, B_r, C_r, D_r, states_r, output)
        if self.option_choice == 7:
            saveDataIntoMatrix("ieee7", A_r, B_r, C_r, D_r, states_r, output)
        if self.option_choice == 8:
            saveDataIntoMatrix("ieee5", A_r, B_r, C_r, D_r, states_r, output)

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
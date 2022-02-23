import cmath
import sys
sys.path.append('../')
from systemExamples.systemExample import SystemExample
from systemExamples.transformationsCsv import Csv
import modalTruncationAlgorithm
import numpy as np
from timeit import default_timer as timer
from saveOutputData import saveDataIntoMatrix
from saveOutputData import saveIEEE34DataIntoMatrix
import results.calculateError as calculateError

class Menu:
    def __init__(self):
        self.loop = True
        self.alpha = 0.1
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
        self.isIEEE34 = False
        self.option_choice = 0

    def switch(self, option_number):
        default = "Invalid input. Please enter a number between 1 and 6 or exit."
        return getattr(self, "option_" + str(option_number), lambda: default)()

    def print_menu(self):
        print(7 * "-", "Spectral Projection Modal Truncation Algorithm's Menu", 7 * "-")
        print("1. Set the minimun reduced order (k)")
        print("2. Set the stability margin (alpha)")
        print("3. Set the IEEE 34 system")
        print("4. Set the IEEE 18 system")
        print("5. Set the IEEE 7 system")
        print("6. Set the IEEE 5 system")
        print("7. Execute Spectral Projection Modal Truncation reduction algorithm")
        print("e. Exit")
        print(69 * "-")
        option_choice = input("Enter an option [1-7/e]: ")
        print("Option " + option_choice + " chosen")
        self.option_choice = option_choice
        return option_choice

    def option_1(self):
        self.reduced_order = input("Enter the value for reduced-order you wish to obtain (k): ")
        self.reduced_order = int(self.reduced_order)

    def option_2(self):
        self.alpha = input("Enter the value for the stability margin (alpha): ")
        self.alpha = float(self.alpha)

    def option_3(self):
        self.A, self.B, self.C, self.D, self.inputs, self.initial_states, self.output = SystemExample.setDataIEEE34SystemExample()
        self.isPartData = True
        self.isIEEE34 = True

    def option_4(self):
        self.A, self.B, self.C, self.D, self.inputs, self.initial_states, self.output = SystemExample.setDataIEEE18SystemExample()
        self.isPartData = False
        self.isIEEE34 = True
     
    def option_5(self):
        self.A, self.B, self.C, self.D, self.inputs, self.initial_states, self.output = SystemExample.setDataIEEE7SystemExample()
        self.isIEEE34 = False

    def option_6(self):
        self.A, self.B, self.C, self.D, self.inputs, self.initial_states, self.output = SystemExample.setDataIEEE5SystemExample()
        self.isIEEE34 = False

    def option_7(self):
        start1 = timer()
        order = np.shape(self.A)[0]
        A_r = self.A
        B_r = self.B
        C_r = self.C
        D_r = self.D

        while order > self.reduced_order:
            start = timer()
            A_r, B_r, C_r, D_r, states_r = modalTruncationAlgorithm.algorithm(A_r, B_r, C_r, D_r, self.inputs, self.initial_states, self.alpha, self.reduced_order)
            order = np.shape(A_r)[0]
            print("Execution time per algorithm execution: %f seconds" % (timer() - start))
    
        end = timer()
        print("Final execution time: %f seconds" % (end - start1))
        print("Reduced order: %i" % order)

        output = np.dot(C_r, states_r) + np.dot(D_r, self.inputs)

        if self.option_choice == 3:
            saveDataIntoMatrix("ieee34", A_r, B_r, C_r, D_r, states_r, output)
        if self.option_choice == 4:
            saveDataIntoMatrix("ieee18", A_r, B_r, C_r, D_r, states_r, output)
        if self.option_choice == 5:
            saveDataIntoMatrix("ieee7", A_r, B_r, C_r, D_r, states_r, output)
        if self.option_choice == 6:
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
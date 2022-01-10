import sys
sys.path.append('../')
from systemExamples.systemExample import SystemExample
from systemExamples.transformationsCsv import Csv
import modalTruncationAlgorithm
import numpy as np
import time

class Menu:
    def __init__(self):
        self.loop = True
        self.alpha = 0
        self.error_tolerance = 0
        self.reduced_order = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.start_time = 0


    def switch(self, option_number):
        default = "Invalid input. Please enter a number between 1 and 6 or exit."
        return getattr(self, "option_" + str(option_number), lambda: default)()

    def print_menu(self):
        print(30 * "-", "MENU", 30 * "-")
        print("1. Set the stability margin (alpha)")
        print("2. Set the error tolerance (e)")
        print("3. Set the minimun reduced order (k)")
        print("4. Set the IEEE34 partial data system")
        print("5. Set the IEEE34 system")
        print("6. Execute Spectral Projection Modal Truncation reduction algorithm")
        print("e. Exit")
        print(67 * "-")
        option_choice = input("Enter an option [1-6/e]: ")
        print("Option " + option_choice + " chosen")
        return option_choice

    def option_1(self):
        self.alpha = input("Enter the value for the stability margin (alpha): ")

    def option_2(self):
        self.error_tolerance = input("Enter the value for the error tolerance (e): ")

    def option_3(self):
        self.reduced_order = input("Enter the value for reduced-order you wish to obtain (k): ")

    def option_4(self):
        self.A, self.B, self.C, self.D = SystemExample.setPartDataIEEE34SystemExample()
        self.reduced_order = 15

    def option_5(self):
        self.A, self.B, self.C, self.D = SystemExample.setDataIEEE34SystemExample()
        self.reduced_order = 50

    def option_6(self):
        order = np.shape(self.A)[0]

        self.alpha = 0.1

        while order > self.reduced_order:
            A_r, B_r, C_r, D_r = modalTruncationAlgorithm.algorithm(self.A, self.B, self.C, self.D, self.alpha)
            self.A = A_r
            self.B = B_r
            self.C = C_r
            self.D = D_r
            order = np.shape(A_r)[0]
            print("Execution time per algorithm execution: %s seconds" % (time.time() - self.start_time))
    
        self.reduced_order = np.shape(A_r)[0]
        print("Final execution time: %s seconds" % (time.time() - self.start_time))
        print("Reduced order: %i" % self.reduced_order)
        Csv.transformMatrixToCVS(A_r, "A_spectralProjection")
        Csv.transformMatrixToCVS(B_r, "B_spectralProjection")
        Csv.transformMatrixToCVS(C_r, "C_spectralProjection")
        Csv.transformMatrixToCVS(D_r, "D_spectralProjection")

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
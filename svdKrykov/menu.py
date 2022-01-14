import sys
sys.path.append('../')
from systemExamples.systemExample import SystemExample
from systemExamples.transformationsCsv import Csv
import interactiveSvdKrylov
import time
import numpy as np

class Menu:
    def __init__(self):
        self.loop = True
        self.interpolation_points = 5
        self.error_tolerance = 0.1
        self.reduced_order = 15
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.inputs = 0
        self.start_time = 0
        self.isPartData = False


    def switch(self, option_number):
        default = "Invalid input. Please enter a number between 1 and 5 or exit."
        return getattr(self, "option_" + str(option_number), lambda: default)()

    def print_menu(self):
        print(30 * "-", "MENU", 30 * "-")
        print("1. Set the reduced-order to be achieved (k)")
        print("2. Set the error tolerance (e)")
        print("3. Set the IEEE34 partial data system")
        print("4. Set the IEEE34 system")
        print("5. Execute Interactive SVD-Krylov reduction algorithm")
        print("e. Exit")
        print(67 * "-")
        option_choice = input("Enter an option [1-5/e]: ")
        print("Option " + option_choice + " chosen")
        return option_choice

    def option_1(self):
        self.reduced_order = input("Enter the value for the reduced-order you wish to obtain (k): ")

    def option_2(self):
        self.error_tolerance = input("Enter the value for the error tolerance (e): ")

    def option_3(self):
        self.A, self.B, self.C, self.D = SystemExample.setPartDataIEEE34SystemExample()
        self.inputs = Csv.transformComplexCsvToMatrix('ieee34_part_data_inputs')
        self.reduced_order = 15
        self.interpolation_points = int(self.reduced_order/np.shape(self.B)[1])
        self.isPartData = True

    def option_4(self):
        self.A, self.B, self.C, self.D = SystemExample.setDataIEEE34SystemExample()
        self.inputs = Csv.transformComplexCsvToMatrix('ieee34_data_inputs')
        self.reduced_order = 50
        self.interpolation_points = int(self.reduced_order/np.shape(self.B)[1])
        self.isPartData = False

    def option_5(self):
        self.start_time = time.time()
        A_r, B_r, C_r, D_r, states_r = interactiveSvdKrylov.algorithm(
            self.A, self.B, self.C, self.D, self.inputs, self.interpolation_points, self.error_tolerance)
        self.reduced_order = np.shape(A_r)[0]
        print("Execution time: %s seconds" % (time.time() - self.start_time))
        print("Reduced order: %i" % self.reduced_order)

        if self.isPartData:
            Csv.transformMatrixToCVS(A_r, "part_A_svdKrylov")
            Csv.transformMatrixToCVS(B_r, "part_B_svdKrylov")
            Csv.transformMatrixToCVS(C_r, "part_C_svdKrylov")
            Csv.transformMatrixToCVS(D_r, "part_D_svdKrylov")
            Csv.transformMatrixToCVS(states_r, "part_states_svdKrylov")

        else:
            Csv.transformMatrixToCVS(A_r, "A_svdKrylov")
            Csv.transformMatrixToCVS(B_r, "B_svdKrylov")
            Csv.transformMatrixToCVS(C_r, "C_svdKrylov")
            Csv.transformMatrixToCVS(D_r, "D_svdKrylov")
            Csv.transformMatrixToCVS(states_r, "states_svdKrylov")

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
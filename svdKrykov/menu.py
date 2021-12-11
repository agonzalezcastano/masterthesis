import systemNewEngland
import systemExample
import interactiveSvdKrylov

class Menu:
    def __init__(self):
        self.loop = True
        self.error_tolerance = 0
        self.reduced_order = 0
        self.time_step = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0


    def switch(self, option_number):
        default = "Invalid input. Please enter a number between 1 and 6 or exit."
        return getattr(self, "option_" + str(option_number), lambda: default)()

    def print_menu(self):
        print(30 * "-", "MENU", 30 * "-")
        print("1. Set the reduced-order to be achieved (k)")
        print("2. Set the error tolerance (e)")
        print("3. Set the time step lenght value (t)")
        print("4. Set the system")
        print("5. Set the New England system")
        print("6. Execute Interactive SVD-Krylov reduction algorithm")
        print("e. Exit")
        print(67 * "-")
        option_choice = input("Enter an option [1-6/e]: ")
        print("Option " + option_choice + " chosen")
        return option_choice

    def option_1(self):
        self.reduced_order = input("Enter the value for the reduced-order (k): ")

    def option_2(self):
        self.error_tolerance = input("Enter the value for the error tolerance (e): ")

    def option_3(self):
        self.time_step = input("Enter the value for the time step (t): ")

    def option_4(self):
        self.A, self.B, self.C, self.D = systemExample.setSystemExample(self.time_step)

    def option_5(self):
        self.A, self.B, self.C, self.D = systemNewEngland.setSystemNewEngland(self.time_step)

    def option_6(self):
        print("The reduced-order is " + self.reduced_order)
        
        G_r = interactiveSvdKrylov.algorithm(
            self.A, self.B, self.C, self.D, self.reduced_order, self.time_step, self.error_tolerance)
        print("The reduced system is: " + G_r)

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
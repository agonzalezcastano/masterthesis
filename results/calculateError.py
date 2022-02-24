import numpy as np

def relative_error(initial_output, output):
    error = np.absolute(np.real(initial_output) - np.real(output))/np.absolute(np.real(initial_output))
    return error

def print_errors_IEEE5(initial_output, output):
    print_relative_error_IEEE5_bus_800(initial_output, output)
    print_relative_error_IEEE5_bus_806(initial_output, output)

def print_errors_IEEE7(initial_output, output):
    print_relative_error_IEEE7_bus_800(initial_output, output)
    print_relative_error_IEEE7_bus_812(initial_output, output)

def print_errors_IEEE18(initial_output, output):
    print_relative_error_IEEE18_bus_800(initial_output, output)
    print_relative_error_IEEE18_bus_812(initial_output, output)
    print_relative_error_IEEE18_bus_830(initial_output, output)

def print_errors_IEEE34(initial_output, output):
    print_relative_error_IEEE34_bus_800(initial_output, output)
    print_relative_error_IEEE34_bus_812(initial_output, output)
    print_relative_error_IEEE34_bus_830(initial_output, output)
    print_relative_error_IEEE34_bus_836(initial_output, output)
    print_relative_error_IEEE34_bus_846(initial_output, output)
    print_relative_error_IEEE34_bus_858(initial_output, output)

def print_relative_error_IEEE5_bus_806(initial_output, output):
    relative_error_voltage_A_bus_806 = relative_error(initial_output[4], output[4])
    print("Relative error voltage A bus 806: ")
    print(relative_error_voltage_A_bus_806)

    relative_error_voltage_B_bus_806 = relative_error(initial_output[5], output[5])
    print("Relative error voltage B bus 806: ")
    print(relative_error_voltage_B_bus_806)

    relative_error_voltage_C_bus_806 = relative_error(initial_output[6], output[6])
    print("Relative error voltage C bus 806: ")
    print(relative_error_voltage_C_bus_806)

    relative_error_current_A_bus_806 = relative_error(initial_output[10], output[10])
    print("Relative error current A bus 806: ")
    print(relative_error_current_A_bus_806)

    relative_error_current_B_bus_806 = relative_error(initial_output[11], output[11])
    print("Relative error current B bus 806: ")
    print(relative_error_current_B_bus_806)

    relative_error_current_C_bus_806 = relative_error(initial_output[12], output[12])
    print("Relative error current C bus 806: ")
    print(relative_error_current_C_bus_806)

def print_relative_error_IEEE5_bus_800(initial_output, output):
    relative_error_voltage_A_bus_800 = relative_error(initial_output[1], output[1])
    print("Relative error voltage A bus 800: ")
    print(relative_error_voltage_A_bus_800)

    relative_error_voltage_B_bus_800 = relative_error(initial_output[2], output[2])
    print("Relative error voltage B bus 800: ")
    print(relative_error_voltage_B_bus_800)

    relative_error_voltage_C_bus_800 = relative_error(initial_output[3], output[3])
    print("Relative error voltage C bus 800: ")
    print(relative_error_voltage_C_bus_800)

    relative_error_current_A_bus_800 = relative_error(initial_output[7], output[7])
    print("Relative error current A bus 800: ")
    print(relative_error_current_A_bus_800)

    relative_error_current_B_bus_800 = relative_error(initial_output[8], output[8])
    print("Relative error current B bus 800: ")
    print(relative_error_current_B_bus_800)

    relative_error_current_C_bus_800 = relative_error(initial_output[9], output[9])
    print("Relative error current C bus 800: ")
    print(relative_error_current_C_bus_800)

def print_relative_error_IEEE7_bus_800(initial_output, output):
    relative_error_voltage_A_bus_800 = relative_error(initial_output[4], output[4])
    print("Relative error voltage A bus 800: ")
    print(relative_error_voltage_A_bus_800)

    relative_error_voltage_B_bus_800 = relative_error(initial_output[5], output[5])
    print("Relative error voltage B bus 800: ")
    print(relative_error_voltage_B_bus_800)

    relative_error_voltage_C_bus_800 = relative_error(initial_output[6], output[6])
    print("Relative error voltage C bus 800: ")
    print(relative_error_voltage_C_bus_800)

    relative_error_current_A_bus_800 = relative_error(initial_output[10], output[10])
    print("Relative error current A bus 800: ")
    print(relative_error_current_A_bus_800)

    relative_error_current_B_bus_800 = relative_error(initial_output[11], output[11])
    print("Relative error current B bus 800: ")
    print(relative_error_current_B_bus_800)

    relative_error_current_C_bus_800 = relative_error(initial_output[12], output[12])
    print("Relative error current C bus 800: ")
    print(relative_error_current_C_bus_800)

def print_relative_error_IEEE7_bus_812(initial_output, output):
    relative_error_voltage_A_bus_812 = relative_error(initial_output[0], output[0])
    print("Relative error voltage A bus 812: ")
    print(relative_error_voltage_A_bus_812)

    relative_error_voltage_B_bus_812 = relative_error(initial_output[1], output[1])
    print("Relative error voltage B bus 812: ")
    print(relative_error_voltage_B_bus_812)

    relative_error_voltage_C_bus_812 = relative_error(initial_output[2], output[2])
    print("Relative error voltage C bus 812: ")
    print(relative_error_voltage_C_bus_812)

    relative_error_current_A_bus_812 = relative_error(initial_output[7], output[7])
    print("Relative error current A bus 812: ")
    print(relative_error_current_A_bus_812)

    relative_error_current_B_bus_812 = relative_error(initial_output[8], output[8])
    print("Relative error current B bus 812: ")
    print(relative_error_current_B_bus_812)

    relative_error_current_C_bus_812 = relative_error(initial_output[9], output[9])
    print("Relative error current C bus 812: ")
    print(relative_error_current_C_bus_812)

def print_relative_error_IEEE34_bus_800(initial_output, output):
    relative_error_voltage_A_bus_800 = relative_error(initial_output[4], output[4])
    print("Relative error voltage A bus 800: ")
    print(relative_error_voltage_A_bus_800)

    relative_error_voltage_B_bus_800 = relative_error(initial_output[5], output[5])
    print("Relative error voltage B bus 800: ")
    print(relative_error_voltage_B_bus_800)

    relative_error_voltage_C_bus_800 = relative_error(initial_output[6], output[6])
    print("Relative error voltage C bus 800: ")
    print(relative_error_voltage_C_bus_800)

    relative_error_current_A_bus_800 = relative_error(initial_output[28], output[28])
    print("Relative error current A bus 800: ")
    print(relative_error_current_A_bus_800)

    relative_error_current_B_bus_800 = relative_error(initial_output[29], output[29])
    print("Relative error current B bus 800: ")
    print(relative_error_current_B_bus_800)

    relative_error_current_C_bus_800 = relative_error(initial_output[30], output[30])
    print("Relative error current C bus 800: ")
    print(relative_error_current_C_bus_800)

def print_relative_error_IEEE34_bus_812(initial_output, output):
    relative_error_voltage_A_bus_812 = relative_error(initial_output[0], output[0])
    print("Relative error voltage A bus 812: ")
    print(relative_error_voltage_A_bus_812)

    relative_error_voltage_B_bus_812 = relative_error(initial_output[1], output[1])
    print("Relative error voltage B bus 812: ")
    print(relative_error_voltage_B_bus_812)

    relative_error_voltage_C_bus_812 = relative_error(initial_output[2], output[2])
    print("Relative error voltage C bus 812: ")
    print(relative_error_voltage_C_bus_812)

    relative_error_current_A_bus_812 = relative_error(initial_output[25], output[25])
    print("Relative error current A bus 812: ")
    print(relative_error_current_A_bus_812)

    relative_error_current_B_bus_812 = relative_error(initial_output[26], output[26])
    print("Relative error current B bus 812: ")
    print(relative_error_current_B_bus_812)

    relative_error_current_C_bus_812 = relative_error(initial_output[27], output[27])
    print("Relative error current C bus 812: ")
    print(relative_error_current_C_bus_812)

def print_relative_error_IEEE34_bus_830(initial_output, output):
    relative_error_voltage_A_bus_830 = relative_error(initial_output[7], output[7])
    print("Relative error voltage A bus 830: ")
    print(relative_error_voltage_A_bus_830)

    relative_error_voltage_B_bus_830 = relative_error(initial_output[8], output[8])
    print("Relative error voltage B bus 830: ")
    print(relative_error_voltage_B_bus_830)

    relative_error_voltage_C_bus_830 = relative_error(initial_output[9], output[9])
    print("Relative error voltage C bus 830: ")
    print(relative_error_voltage_C_bus_830)

    relative_error_current_A_bus_830 = relative_error(initial_output[31], output[31])
    print("Relative error current A bus 830: ")
    print(relative_error_current_A_bus_830)

    relative_error_current_B_bus_830 = relative_error(initial_output[32], output[32])
    print("Relative error current B bus 830: ")
    print(relative_error_current_B_bus_830)

    relative_error_current_C_bus_830 = relative_error(initial_output[33], output[33])
    print("Relative error current C bus 830: ")
    print(relative_error_current_C_bus_830)

def print_relative_error_IEEE34_bus_836(initial_output, output):
    relative_error_voltage_A_bus_836 = relative_error(initial_output[22], output[22])
    print("Relative error voltage A bus 836: ")
    print(relative_error_voltage_A_bus_836)

    relative_error_voltage_B_bus_836 = relative_error(initial_output[23], output[23])
    print("Relative error voltage B bus 836: ")
    print(relative_error_voltage_B_bus_836)

    relative_error_voltage_C_bus_836 = relative_error(initial_output[24], output[24])
    print("Relative error voltage C bus 836: ")
    print(relative_error_voltage_C_bus_836)

    relative_error_current_A_bus_836 = relative_error(initial_output[46], output[46])
    print("Relative error current A bus 836: ")
    print(relative_error_current_A_bus_836)

    relative_error_current_B_bus_836 = relative_error(initial_output[47], output[47])
    print("Relative error current B bus 836: ")
    print(relative_error_current_B_bus_836)

    relative_error_current_C_bus_836 = relative_error(initial_output[48], output[48])
    print("Relative error current C bus 836: ")
    print(relative_error_current_C_bus_836)

def print_relative_error_IEEE34_bus_846(initial_output, output):
    relative_error_voltage_A_bus_846 = relative_error(initial_output[10], output[10])
    print("Relative error voltage A bus 846: ")
    print(relative_error_voltage_A_bus_846)

    relative_error_voltage_B_bus_846 = relative_error(initial_output[11], output[11])
    print("Relative error voltage B bus 846: ")
    print(relative_error_voltage_B_bus_846)

    relative_error_voltage_C_bus_846 = relative_error(initial_output[12], output[12])
    print("Relative error voltage C bus 846: ")
    print(relative_error_voltage_C_bus_846)

    relative_error_current_A_bus_846 = relative_error(initial_output[34], output[34])
    print("Relative error current A bus 846: ")
    print(relative_error_current_A_bus_846)

    relative_error_current_B_bus_846 = relative_error(initial_output[35], output[35])
    print("Relative error current B bus 846: ")
    print(relative_error_current_B_bus_846)

    relative_error_current_C_bus_846 = relative_error(initial_output[36], output[36])
    print("Relative error current C bus 846: ")
    print(relative_error_current_C_bus_846)

def print_relative_error_IEEE34_bus_858(initial_output, output):
    relative_error_voltage_A_bus_858 = relative_error(initial_output[13], output[13])
    print("Relative error voltage A bus 858: ")
    print(relative_error_voltage_A_bus_858)

    relative_error_voltage_B_bus_858 = relative_error(initial_output[14], output[14])
    print("Relative error voltage B bus 858: ")
    print(relative_error_voltage_B_bus_858)

    relative_error_voltage_C_bus_858 = relative_error(initial_output[15], output[15])
    print("Relative error voltage C bus 858: ")
    print(relative_error_voltage_C_bus_858)

    relative_error_current_A_bus_858 = relative_error(initial_output[38], output[38])
    print("Relative error current A bus 858: ")
    print(relative_error_current_A_bus_858)

    relative_error_current_B_bus_858 = relative_error(initial_output[39], output[39])
    print("Relative error current B bus 858: ")
    print(relative_error_current_B_bus_858)

    relative_error_current_C_bus_858 = relative_error(initial_output[40], output[40])
    print("Relative error current C bus 858: ")
    print(relative_error_current_C_bus_858)

def print_relative_error_IEEE18_bus_830(initial_output, output):
    relative_error_voltage_A_bus_830 = relative_error(initial_output[7], output[7])
    print("Relative error voltage A bus 830: ")
    print(relative_error_voltage_A_bus_830)

    relative_error_voltage_B_bus_830 = relative_error(initial_output[8], output[8])
    print("Relative error voltage B bus 830: ")
    print(relative_error_voltage_B_bus_830)

    relative_error_voltage_C_bus_830 = relative_error(initial_output[9], output[9])
    print("Relative error voltage C bus 830: ")
    print(relative_error_voltage_C_bus_830)

    relative_error_current_A_bus_830 = relative_error(initial_output[16], output[16])
    print("Relative error current A bus 830: ")
    print(relative_error_current_A_bus_830)

    relative_error_current_B_bus_830 = relative_error(initial_output[17], output[17])
    print("Relative error current B bus 830: ")
    print(relative_error_current_B_bus_830)

    relative_error_current_C_bus_830 = relative_error(initial_output[18], output[18])
    print("Relative error current C bus 830: ")
    print(relative_error_current_C_bus_830)

def print_relative_error_IEEE18_bus_800(initial_output, output):
    relative_error_voltage_A_bus_800 = relative_error(initial_output[4], output[4])
    print("Relative error voltage A bus 800: ")
    print(relative_error_voltage_A_bus_800)

    relative_error_voltage_B_bus_800 = relative_error(initial_output[5], output[5])
    print("Relative error voltage B bus 800: ")
    print(relative_error_voltage_B_bus_800)

    relative_error_voltage_C_bus_800 = relative_error(initial_output[6], output[6])
    print("Relative error voltage C bus 800: ")
    print(relative_error_voltage_C_bus_800)

    relative_error_current_A_bus_800 = relative_error(initial_output[13], output[13])
    print("Relative error current A bus 800: ")
    print(relative_error_current_A_bus_800)

    relative_error_current_B_bus_800 = relative_error(initial_output[14], output[14])
    print("Relative error current B bus 800: ")
    print(relative_error_current_B_bus_800)

    relative_error_current_C_bus_800 = relative_error(initial_output[15], output[15])
    print("Relative error current C bus 800: ")
    print(relative_error_current_C_bus_800)

def print_relative_error_IEEE18_bus_812(initial_output, output):
    relative_error_voltage_A_bus_812 = relative_error(initial_output[0], output[0])
    print("Relative error voltage A bus 812: ")
    print(relative_error_voltage_A_bus_812)

    relative_error_voltage_B_bus_812 = relative_error(initial_output[1], output[1])
    print("Relative error voltage B bus 812: ")
    print(relative_error_voltage_B_bus_812)

    relative_error_voltage_C_bus_812 = relative_error(initial_output[2], output[2])
    print("Relative error voltage C bus 812: ")
    print(relative_error_voltage_C_bus_812)

    relative_error_current_A_bus_812 = relative_error(initial_output[10], output[10])
    print("Relative error current A bus 812: ")
    print(relative_error_current_A_bus_812)

    relative_error_current_B_bus_812 = relative_error(initial_output[11], output[11])
    print("Relative error current B bus 812: ")
    print(relative_error_current_B_bus_812)

    relative_error_current_C_bus_812 = relative_error(initial_output[12], output[12])
    print("Relative error current C bus 812: ")
    print(relative_error_current_C_bus_812)

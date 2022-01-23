import numpy as np

def rms_error(initial_output, output):
    error = np.square(np.subtract(np.real(initial_output), np.real(output))).mean()
    return error

def relative_error(initial_output, output):
    error = np.absolute(np.real(initial_output) - np.real(output))/np.absolute(np.real(initial_output))
    return error

def steady_state_error(initial_output, output):
    error =  initial_output - output
    return error

def print_relative_error_IEEE34_bus_800(initial_output, output):
    relative_error_voltage_A_bus_800 = relative_error(initial_output[10], output[10])
    print("Relative error voltage A bus 800: ")
    print(relative_error_voltage_A_bus_800)

    relative_error_voltage_B_bus_800 = relative_error(initial_output[11], output[11])
    print("Relative error voltage B bus 800: ")
    print(relative_error_voltage_B_bus_800)

    relative_error_voltage_C_bus_800 = relative_error(initial_output[12], output[12])
    print("Relative error voltage C bus 800: ")
    print(relative_error_voltage_C_bus_800)

    relative_error_current_A_bus_800 = relative_error(initial_output[34], output[34])
    print("Relative error current A bus 800: ")
    print(relative_error_current_A_bus_800)

    relative_error_current_B_bus_800 = relative_error(initial_output[35], output[35])
    print("Relative error current B bus 800: ")
    print(relative_error_current_B_bus_800)

    relative_error_current_C_bus_800 = relative_error(initial_output[36], output[36])
    print("Relative error current C bus 800: ")
    print(relative_error_current_C_bus_800)

def print_relative_error_IEEE34_bus_812(initial_output, output):
    relative_error_voltage_A_bus_812 = relative_error(initial_output[7], output[7])
    print("Relative error voltage A bus 812: ")
    print(relative_error_voltage_A_bus_812)

    relative_error_voltage_B_bus_812 = relative_error(initial_output[8], output[8])
    print("Relative error voltage B bus 812: ")
    print(relative_error_voltage_B_bus_812)

    relative_error_voltage_C_bus_812 = relative_error(initial_output[9], output[9])
    print("Relative error voltage C bus 812: ")
    print(relative_error_voltage_C_bus_812)

    relative_error_current_A_bus_812 = relative_error(initial_output[31], output[31])
    print("Relative error current A bus 812: ")
    print(relative_error_current_A_bus_812)

    relative_error_current_B_bus_812 = relative_error(initial_output[32], output[32])
    print("Relative error current B bus 812: ")
    print(relative_error_current_B_bus_812)

    relative_error_current_C_bus_812 = relative_error(initial_output[33], output[33])
    print("Relative error current C bus 812: ")
    print(relative_error_current_C_bus_812)

def print_relative_error_IEEE34_bus_830(initial_output, output):
    relative_error_voltage_A_bus_830 = relative_error(initial_output[13], output[13])
    print("Relative error voltage A bus 830: ")
    print(relative_error_voltage_A_bus_830)

    relative_error_voltage_B_bus_830 = relative_error(initial_output[14], output[14])
    print("Relative error voltage B bus 830: ")
    print(relative_error_voltage_B_bus_830)

    relative_error_voltage_C_bus_830 = relative_error(initial_output[15], output[15])
    print("Relative error voltage C bus 830: ")
    print(relative_error_voltage_C_bus_830)

    relative_error_current_A_bus_830 = relative_error(initial_output[37], output[37])
    print("Relative error current A bus 830: ")
    print(relative_error_current_A_bus_830)

    relative_error_current_B_bus_830 = relative_error(initial_output[38], output[38])
    print("Relative error current B bus 830: ")
    print(relative_error_current_B_bus_830)

    relative_error_current_C_bus_830 = relative_error(initial_output[39], output[39])
    print("Relative error current C bus 830: ")
    print(relative_error_current_C_bus_830)

def print_relative_error_IEEE34_bus_836(initial_output, output):
    relative_error_voltage_A_bus_836 = relative_error(initial_output[16], output[16])
    print("Relative error voltage A bus 836: ")
    print(relative_error_voltage_A_bus_836)

    relative_error_voltage_B_bus_836 = relative_error(initial_output[17], output[17])
    print("Relative error voltage B bus 836: ")
    print(relative_error_voltage_B_bus_836)

    relative_error_voltage_C_bus_836 = relative_error(initial_output[18], output[18])
    print("Relative error voltage C bus 836: ")
    print(relative_error_voltage_C_bus_836)

    relative_error_current_A_bus_836 = relative_error(initial_output[40], output[40])
    print("Relative error current A bus 836: ")
    print(relative_error_current_A_bus_836)

    relative_error_current_B_bus_836 = relative_error(initial_output[41], output[41])
    print("Relative error current B bus 836: ")
    print(relative_error_current_B_bus_836)

    relative_error_current_C_bus_836 = relative_error(initial_output[42], output[42])
    print("Relative error current C bus 836: ")
    print(relative_error_current_C_bus_836)

def print_relative_error_IEEE34_bus_846(initial_output, output):
    relative_error_voltage_A_bus_846 = relative_error(initial_output[19], output[19])
    print("Relative error voltage A bus 846: ")
    print(relative_error_voltage_A_bus_846)

    relative_error_voltage_B_bus_846 = relative_error(initial_output[20], output[20])
    print("Relative error voltage B bus 846: ")
    print(relative_error_voltage_B_bus_846)

    relative_error_voltage_C_bus_846 = relative_error(initial_output[21], output[21])
    print("Relative error voltage C bus 846: ")
    print(relative_error_voltage_C_bus_846)

    relative_error_current_A_bus_846 = relative_error(initial_output[43], output[43])
    print("Relative error current A bus 846: ")
    print(relative_error_current_A_bus_846)

    relative_error_current_B_bus_846 = relative_error(initial_output[44], output[44])
    print("Relative error current B bus 846: ")
    print(relative_error_current_B_bus_846)

    relative_error_current_C_bus_846 = relative_error(initial_output[45], output[45])
    print("Relative error current C bus 846: ")
    print(relative_error_current_C_bus_846)

def print_relative_error_IEEE123_bus_30(initial_output, output):
    relative_error_voltage_A_bus_30 = relative_error(initial_output[6], output[6])
    print("Relative error voltage A bus 30: ")
    print(relative_error_voltage_A_bus_30)

    relative_error_voltage_B_bus_30 = relative_error(initial_output[7], output[7])
    print("Relative error voltage B bus 30: ")
    print(relative_error_voltage_B_bus_30)

    relative_error_voltage_C_bus_30 = relative_error(initial_output[8], output[8])
    print("Relative error voltage C bus 30: ")
    print(relative_error_voltage_C_bus_30)

    relative_error_current_A_bus_30 = relative_error(initial_output[45], output[45])
    print("Relative error current A bus 30: ")
    print(relative_error_current_A_bus_30)

    relative_error_current_B_bus_30 = relative_error(initial_output[46], output[46])
    print("Relative error current B bus 30: ")
    print(relative_error_current_B_bus_30)

    relative_error_current_C_bus_30 = relative_error(initial_output[47], output[47])
    print("Relative error current C bus 30: ")
    print(relative_error_current_C_bus_30)

def print_relative_error_IEEE123_bus_60(initial_output, output):
    relative_error_voltage_A_bus_60 = relative_error(initial_output[24], output[24])
    print("Relative error voltage A bus 60: ")
    print(relative_error_voltage_A_bus_60)

    relative_error_voltage_B_bus_60 = relative_error(initial_output[25], output[25])
    print("Relative error voltage B bus 60: ")
    print(relative_error_voltage_B_bus_60)

    relative_error_voltage_C_bus_60 = relative_error(initial_output[26], output[26])
    print("Relative error voltage C bus 60: ")
    print(relative_error_voltage_C_bus_60)

    relative_error_current_A_bus_60 = relative_error(initial_output[63], output[63])
    print("Relative error current A bus 60: ")
    print(relative_error_current_A_bus_60)

    relative_error_current_B_bus_60 = relative_error(initial_output[64], output[64])
    print("Relative error current B bus 60: ")
    print(relative_error_current_B_bus_60)

    relative_error_current_C_bus_60 = relative_error(initial_output[65], output[65])
    print("Relative error current C bus 60: ")
    print(relative_error_current_C_bus_60)

def print_relative_error_IEEE123_bus_83(initial_output, output):
    relative_error_voltage_A_bus_83 = relative_error(initial_output[15], output[15])
    print("Relative error voltage A bus 83: ")
    print(relative_error_voltage_A_bus_83)

    relative_error_voltage_B_bus_83 = relative_error(initial_output[16], output[16])
    print("Relative error voltage B bus 83: ")
    print(relative_error_voltage_B_bus_83)

    relative_error_voltage_C_bus_83 = relative_error(initial_output[17], output[17])
    print("Relative error voltage C bus 83: ")
    print(relative_error_voltage_C_bus_83)

    relative_error_current_A_bus_83 = relative_error(initial_output[54], output[54])
    print("Relative error current A bus 83: ")
    print(relative_error_current_A_bus_83)

    relative_error_current_B_bus_83 = relative_error(initial_output[55], output[55])
    print("Relative error current B bus 83: ")
    print(relative_error_current_B_bus_83)

    relative_error_current_C_bus_83 = relative_error(initial_output[56], output[56])
    print("Relative error current C bus 83: ")
    print(relative_error_current_C_bus_83)

def print_relative_error_IEEE123_bus_95(initial_output, output):
    relative_error_voltage_A_bus_95 = relative_error(initial_output[12], output[12])
    print("Relative error voltage A bus 95: ")
    print(relative_error_voltage_A_bus_95)

    relative_error_voltage_B_bus_95 = relative_error(initial_output[13], output[13])
    print("Relative error voltage B bus 95: ")
    print(relative_error_voltage_B_bus_95)

    relative_error_voltage_C_bus_95 = relative_error(initial_output[14], output[14])
    print("Relative error voltage C bus 95: ")
    print(relative_error_voltage_C_bus_95)

    relative_error_current_A_bus_95 = relative_error(initial_output[51], output[51])
    print("Relative error current A bus 95: ")
    print(relative_error_current_A_bus_95)

    relative_error_current_B_bus_95 = relative_error(initial_output[52], output[52])
    print("Relative error current B bus 95: ")
    print(relative_error_current_B_bus_95)

    relative_error_current_C_bus_95 = relative_error(initial_output[53], output[53])
    print("Relative error current C bus 95: ")
    print(relative_error_current_C_bus_95)

def print_relative_error_IEEE123_bus_151(initial_output, output):
    relative_error_voltage_A_bus_151 = relative_error(initial_output[33], output[33])
    print("Relative error voltage A bus 151: ")
    print(relative_error_voltage_A_bus_151)

    relative_error_voltage_B_bus_151 = relative_error(initial_output[34], output[34])
    print("Relative error voltage B bus 151: ")
    print(relative_error_voltage_B_bus_151)

    relative_error_voltage_C_bus_151 = relative_error(initial_output[35], output[35])
    print("Relative error voltage C bus 151: ")
    print(relative_error_voltage_C_bus_151)

    relative_error_current_A_bus_151 = relative_error(initial_output[72], output[72])
    print("Relative error current A bus 151: ")
    print(relative_error_current_A_bus_151)

    relative_error_current_B_bus_151 = relative_error(initial_output[73], output[73])
    print("Relative error current B bus 151: ")
    print(relative_error_current_B_bus_151)

    relative_error_current_C_bus_151 = relative_error(initial_output[74], output[74])
    print("Relative error current C bus 151: ")
    print(relative_error_current_C_bus_151)
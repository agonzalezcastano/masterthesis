import numpy as np
import scipy.linalg as linalg

def two_norm_error(A, A_r):
    error = A - A_r
    error = linalg.norm(error, 2)

    print("Output 2-norm error: ")
    print(error)

    return error

def inf_norm_error(A, A_r):
    error = A - A_r
    error = linalg.norm(error, np.inf)

    print("Output inf-norm error: ")
    print(error)

    return error


def steady_state_error(initial_output, inputs, C_r, D_r, states_r):
    error =  initial_output - (np.dot(C_r, states_r) - np.dot(D_r, inputs))

    error_max = np.max(np.absolute(np.real(error)))
    error_min = np.min(np.absolute(np.real(error)))
    
    print("Output steady-state error (vector): ")
    print(error)
    print("Output steady-state max error: ")
    print(error_max)
    print("Output steady-state min error: ")
    print(error_min)

    return error

def dynamic_error(A, B, initial_states, inputs, A_r, B_r, states_r):
    error =  (np.dot(A, initial_states) + np.dot(B, inputs)) - (np.dot(A_r, states_r) + np.dot(B_r, inputs))
    
    print("Output dynamic error: ")
    print(error)

    return error
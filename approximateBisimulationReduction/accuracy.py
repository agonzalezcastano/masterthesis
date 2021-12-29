import numpy as np

def isAccuracyCriterionSatisfied(states_r, state_max):
    status: bool = True
    states_r_indices = np.nonzero(states_r)
    new_states_r = np.empty(0)

    for i in range(0, np.size(states_r_indices[0]), 1):
        state_indice_0 = states_r_indices[0][i]
        state_indice_1 = states_r_indices[1][i]
        new_states_r = np.append(new_states_r, states_r[state_indice_0, state_indice_1])

    for i in range(1, np.size(new_states_r), 1):
        state_r = (new_states_r[i] - new_states_r[i - 1])/(new_states_r[i - 1])
        if state_r < state_max:
            status = True
        else:
            status = False
    return status

def calculateError(C_1, states_1, C_2, states_2):
    error = np.dot(C_1, states_1) - np.dot(C_2, states_2)
    return error

def isErrorBoundSatisfied(C_1, states_1, C_2, states_2, error_tolerance):
    error = calculateError(C_1, states_1, C_2, states_2)
    if error < error_tolerance:
        # Error bound criterion is satisfied
        return True
    else:
        return False

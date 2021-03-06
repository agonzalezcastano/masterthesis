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

def isErrorBoundSatisfied(initial_output, C_2, D_2, inputs_2, states_2, delta, error_tolerance):
    status: bool = True
    error = np.absolute(initial_output - ((C_2 @ states_2) + (D_2 @ inputs_2)))

    for i in range(0, np.shape(error)[0], 1):
        if error[i, 0] < (delta - error_tolerance):
            status = True
        else:
            status = False
    return status

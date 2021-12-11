import numpy as np

def calculateAccuracyCriterion(states_r):
    states_r = (states_r - (states_r -1))/(states_r -1)
    return states_r

def isAccuracyCriterionSatisfied(states_r, states_max):
    states_r = calculateAccuracyCriterion(states_r)
    if states_r < states_max:
        # Accuray criterion is satisfied
        return True
    else:
        return False

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

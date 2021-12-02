import numpy as np
from scipy import signal

def setSystemNewEngland(time_step):
    a = np.array([[0, 1], [0, 0]])
    b = np.array([[0], [1]])
    c = np.array([[1, 0]])
    d = np.array([[0]])

    system_lti = signal.StateSpace(a, b, c, d)
    system_discrete = system_lti.to_discrete(time_step)
    return system_discrete.A, system_discrete.B, system_discrete.C, system_discrete.D

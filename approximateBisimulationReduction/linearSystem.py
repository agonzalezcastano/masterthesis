import scipy.linalg as linalg
import sympy as sp
from numpy.linalg import *
import numpy as np

class LinearSystem:
    def __init__(self, A, B, C, D, inputs, initial_states):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.inputs = inputs
        self.initial_states = initial_states

def solveLinearSystem(G_r: LinearSystem):
    states_r = -np.dot(linalg.pinv(G_r.A), np.dot(G_r.B, G_r.inputs))
    states_r = np.imag(states_r)

    return states_r

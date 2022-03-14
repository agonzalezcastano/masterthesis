import scipy.linalg as linalg
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
    #states_r = linalg.solve(-G_r.A, (0.01-(G_r.B @ G_r.inputs)))
    states_r = linalg.pinv(-G_r.A) @ (0.01-(G_r.B @ G_r.inputs))

    return states_r

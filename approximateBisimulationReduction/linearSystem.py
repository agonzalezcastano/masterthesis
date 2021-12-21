from numpy.matrixlib import matrix
import sympy as sp
from numpy.linalg import *
import numpy as np

class LinearSystem:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.inputs = 0
        self.initial_states = 0

def systemLinearization(f: function, g: function, initial_states, n):
    x, u = sp.symbols('x u')

    diff_f_x = partialDiffOfFX(f, x, initial_states.x, initial_states.u)
    diff_f_u = particalDiffOfFY(f, u, initial_states.x, initial_states.u)
    diff_g_x = partialDiffOfGX(g, x, initial_states.x, initial_states.u)
    diff_g_u = partialDiffOfGY(g, u, initial_states.x, initial_states.u)

    A = diff_f_x - np.dot(np.dot(diff_f_u, inv(diff_g_u)), diff_g_x)
    B = np.identity(n)
    C = diff_g_x
    
    inputs = f(initial_states.x, initial_states.u) - (np.dot(A, initial_states.x))

    lin_model: LinearSystem = LinearSystem(A, B, C, inputs, initial_states)

    return lin_model

def partialDiffOfFX(f, x, x_0, u_0):
    diff_f_x = sp.diff(f, x, (x_0, u_0))
    return diff_f_x

def particalDiffOfFY(f, u, x_0, u_0):
    diff_f_u = sp.diff(f, u, (x_0, u_0))
    return diff_f_u

def partialDiffOfGX(g, x, x_0, u_0):
    diff_g_x = sp.diff(g, x, (x_0, u_0))
    return diff_g_x

def partialDiffOfGY(g, u, x_0, u_0):
    diff_g_u = sp.diff(g, u, (x_0, u_0))
    return diff_g_u

def solveLinearSystem(G_r: LinearSystem):
    x = sp.symbols('x')
    f: function = (np.dot(G_r.A, x)) + (np.dot(G_r.B, G_r.inputs))
    g: function = np.dot(G_r.C, x)

    states_r = solve((f, g), x)
    return states_r

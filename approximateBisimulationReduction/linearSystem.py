import sympy as sp
from numpy.linalg import *
import numpy as np
from sympy.core.function import Function

class LinearSystem:
    def __init__(self, A, B, C, D, inputs, initial_states):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.inputs = inputs
        self.initial_states = initial_states

def systemLinearization(f, g, initial_states, n):
    x, u = sp.symbols('x u')

    diff_f_x = partialDiffOfFX(f, x, initial_states.x, initial_states.u)
    diff_f_u = particalDiffOfFY(f, u, initial_states.x, initial_states.u)
    diff_g_x = partialDiffOfGX(g, x, initial_states.x, initial_states.u)
    diff_g_u = partialDiffOfGY(g, u, initial_states.x, initial_states.u)

    A = diff_f_x - np.dot(np.dot(diff_f_u, inv(diff_g_u)), diff_g_x)
    B = np.identity(n)
    C = diff_g_x
    D = diff_g_u
    
    inputs = f(initial_states.x, initial_states.u) - (np.dot(A, initial_states.x))

    lin_model: LinearSystem = LinearSystem(A, B, C, D, inputs, initial_states)

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
    # x = sp.symbols('x')
    # print("shape G_r.A*x")
    # print(np.shape(G_r.A*x))
    # print("shape b")
    # print(np.shape(-np.dot(G_r.B, np.transpose(G_r.inputs))))
    states_r = solve(G_r.A, -np.dot(G_r.B, np.transpose(G_r.inputs)))

    return states_r

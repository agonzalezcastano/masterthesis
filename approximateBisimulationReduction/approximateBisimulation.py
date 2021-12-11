import numpy as np
import scipy.linalg as linalg
import linearSystem
from linearSystem import LinearSystem
import accuracy

def algorithm(f: function, g: function, inputs, initial_states, reduced_order, states_max, delta_max, error_tolerance):
    A, B, C, inputs, states = linearSystem.systemLinearization(f, g, initial_states, reduced_order)
    G_1 = LinearSystem(A, B, C, inputs, states)
    G_1_stable: LinearSystem = stableSystem(G_1, reduced_order)
    G_r_2: LinearSystem = reduction(G_1_stable)
    states_r = linearSystem.solveLinearSystem(G_r_2)

    while  accuracy.isAccuracyCriterionSatisfied(states_r, states_max):
        A, B, C, inputs, states = linearSystem.systemLinearization(f, g, initial_states, reduced_order)
        G_1 = LinearSystem(A, B, C, inputs, states)
        G_1_stable: LinearSystem = stableSystem(G_1, reduced_order)
        G_r_2: LinearSystem = reduction(G_1_stable)
        states_r = linearSystem.solveLinearSystem(G_r_2)
        p_r_2 = np.dot(G_r_2.C, states_r)
        if accuracy.isErrorBoundSatisfied(G_r_2.C, states_r, G_1_stable.C, G_1_stable.initial_states, error_tolerance):
            return G_r_2, p_r_2
        else:
            reduced_order = reduced_order + 1
    

def stableSystem(G : LinearSystem, reduced_order):
    A  = G.A
    B  = G.B
    C  = G.C
    inputs  = G.inputs
    initial_states  = G.initial_states

    n = np.size(A)
    n_unstable = sum(linalg.eig(A) >= 0)

    if n_unstable > reduced_order:
        print('Dimension of the reduced-order model must be greater than the dimension of the unstable subsystem of G')
    if n_unstable == reduced_order:
        # System is unstable
        # Extraction of the stable subsystem
        A_stable = A[(n_unstable + 1):n, (n_unstable + 1):n]
        B_stable = B[(n_unstable + 1):n, :]
        C_stable = C[:, (n_unstable + 1):n]
    if n_unstable == 0:
        # System is stable
        A_stable = A
        B_stable = B
        C_stable = C

    G_stable = LinearSystem(A_stable, B_stable, C_stable, inputs, initial_states)

    return G_stable

def reduction(G_stable: LinearSystem, H):
    H_inv = linalg.inv(H)
    A_r = np.dot(np.dot(H, G_stable.A), H_inv)
    B_r = np.dot(H, G_stable.B)
    C_r = np.dot(G_stable.C, H_inv)

    inputs = 
    states = 

    G_r = LinearSystem(A_r, B_r, C_r, inputs, states)
    return G_r

def solveLyapunovEquations(A, C):
    eigenvalue_min = min(- np.real(linalg.eig(A)))/1.01

    CC= np.dot(np.transpose(C), C)
    Q = (np.transpose(A) +
        np.dot(eigenvalue_min * np.identity(np.size(A))) * CC) + np.dot(CC, (A + eigenvalue_min * np.identity(np.size(A))))
    [V, D] = linalg.eig(Q)
    D = np.diag(np.dot((np.diag(D)>0), np.diag(D)))
    Q = np.dot(np.dot(V, D), np.transpose(V))
    M = CC + linalg.solve_continuous_lyapunov(np.transpose(A) + eigenvalue_min * np.identity(np.size(A)), Q)

    return M
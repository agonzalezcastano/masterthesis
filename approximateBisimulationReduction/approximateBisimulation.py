import numpy as np
import scipy.linalg as linalg
import linearSystem
from linearSystem import LinearSystem
import accuracy
import decompositionSystem

def algorithm(A, B, C, D, inputs, initial_output, initial_states, reduced_order, states_max, delta_max, error_tolerance):
    states = initial_states
    G_1 = LinearSystem(A, B, C, D, inputs, states)

    G_1 = extractStableSystem(G_1, reduced_order)
    
    eig_vals, eig_vec = linalg.eig(G_1.A)
    n = np.shape(G_1.A)[0]
    n_unstable = sum(eig_vals >= 0)
    H: np.ndarray = calculateSurjectiveMap(n, reduced_order, n_unstable)
    G_r_2: LinearSystem = reduction(G_1, H)
    states_r = linearSystem.solveLinearSystem(G_r_2)

    while  accuracy.isAccuracyCriterionSatisfied(states_r, states_max):
        if accuracy.isErrorBoundSatisfied(initial_output, G_r_2.C, G_r_2.D, G_r_2.inputs, states_r, delta_max, error_tolerance):
            eig_vals, eig_vec = linalg.eig(G_r_2.A)
            return G_r_2.A, G_r_2.B, G_r_2.C, G_r_2.D, states_r, reduced_order
        else:
            reduced_order = reduced_order + 1
            H: np.ndarray = calculateSurjectiveMap(n, reduced_order, n_unstable)
            G_r_2: LinearSystem = reduction(G_1, H)
            states_r = linearSystem.solveLinearSystem(G_r_2)

def extractStableSystem(G : LinearSystem, reduced_order):
    A = G.A
    B = G.B
    C = G.C
    D = G.D
    inputs  = G.inputs
    initial_states  = G.initial_states

    eig_vals, eig_vec = linalg.eig(A)
    n_unstable = sum(eig_vals >= 0)

    if n_unstable > reduced_order:
        print('Dimension of the reduced-order model must be greater than the dimension of the unstable subsystem of G')
        print('Dimension of the unstable system is: ')
        print(n_unstable)
    if n_unstable <= reduced_order:
        # System is unstable
        # Extraction of the stable subsystem
        G_s, projection = decompositionSystem.decomposition(G)
        A = G_s.A
        B = G_s.B
        C = G_s.C
        D = G_s.D
        initial_states = G_s.initial_states
    if n_unstable == 0:
        # System is stable
        A = A
        B = B
        C = C
        D = D
        initial_states = initial_states

    G = LinearSystem(A, B, C, D, inputs, initial_states)

    return G

def reduction(G: LinearSystem, H: np.ndarray):
    H_inv = linalg.pinv(H)
    A_r = H @ G.A @ H_inv
    B_r = H @ G.B
    C_r = G.C @ H_inv
    D_r = G.D

    G_r = LinearSystem(A_r, B_r, C_r, D_r, G.inputs, G.initial_states)
    return G_r

def calculateSurjectiveMap(m: int, k: int, n_unstable: int):
    #  Hs is such that the eigenvalues of the matrix Hs * As,1 * Hs+ have all a strictly negative real part
    identity_matrix_m = np.eye(n_unstable + 1, m)
    identity_matrix_k= np.eye(k, m-n_unstable)
    H: np.ndarray = 2 * np.eye(np.shape(identity_matrix_k)[0], np.shape(identity_matrix_m)[1])
    
    return H
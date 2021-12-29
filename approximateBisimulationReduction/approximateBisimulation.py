import numpy as np
import scipy.linalg as linalg
from scipy.linalg import decomp_cholesky
import linearSystem
from linearSystem import LinearSystem
import accuracy
import decompositionSystem

def algorithm(A, B, C, D, inputs, initial_states, reduced_order, states_max, delta_max, error_tolerance):
    # A, B, C, inputs, states = linearSystem.systemLinearization(f, g, initial_states, reduced_order)
    states = initial_states
    G_1 = LinearSystem(A, B, C, D, inputs, states)
    G_1_stable, projection = extractStableSystem(G_1, reduced_order)

    eig_vals, eig_vec = linalg.eig(G_1_stable.A)
    n = np.shape(G_1_stable.A)[0]
    n_unstable = sum(eig_vals >= 0)
    H: np.ndarray = calculateSurjectiveMap(n, reduced_order, n_unstable, G_1_stable)
    G_r_2: LinearSystem = reduction(G_1_stable, H)
    states_r = linearSystem.solveLinearSystem(G_r_2)

    while  accuracy.isAccuracyCriterionSatisfied(states_r, states_max):
        # A, B, C, inputs, states = linearSystem.systemLinearization(f, g, initial_states, reduced_order)
        G_1 = LinearSystem(A, B, C, D, inputs, states)
        G_1_stable, projection = extractStableSystem(G_1, reduced_order)
        H: np.ndarray = calculateSurjectiveMap(n, reduced_order, n_unstable, G_1_stable)
        G_r_2: LinearSystem = reduction(G_1_stable, H)
        states_r = linearSystem.solveLinearSystem(G_r_2)
        p_r_2 = np.dot(G_r_2.C, states_r)
        if accuracy.isErrorBoundSatisfied(G_r_2.C, states_r, G_1_stable.C, G_1_stable.initial_states, error_tolerance):
            return G_r_2, p_r_2
        else:
            reduced_order = reduced_order + 1

def extractStableSystem(G : LinearSystem, reduced_order):
    A  = G.A
    B  = G.B
    C  = G.C
    D = G.D
    inputs  = G.inputs
    initial_states  = G.initial_states

    eig_vals, eig_vec = linalg.eig(A)

    n = np.shape(A)[0]
    n_unstable = sum(eig_vals >= 0)

    if n_unstable > reduced_order:
        print('Dimension of the reduced-order model must be greater than the dimension of the unstable subsystem of G')
    if n_unstable == reduced_order:
        # System is unstable
        # Extraction of the stable subsystem
        G_s, projection = decompositionSystem.decomposition(G)
        A_stable = G_s.A
        B_stable = G_s.B
        C_stable = G_s.C
        D_stable = G_s.D
    if n_unstable == 0:
        # System is stable
        A_stable = A
        B_stable = B
        C_stable = C
        D_stable = D
        projection = np.identity(n)

    G_stable = LinearSystem(A_stable, B_stable, C_stable, D_stable, inputs, initial_states)

    return G_stable, projection

def reduction(G_stable: LinearSystem, H: np.ndarray):
    H_inv = linalg.inv(H)
    A_r = np.dot(np.dot(H, G_stable.A), H_inv)
    B_r = np.dot(H, G_stable.B)
    C_r = np.dot(G_stable.C, H_inv)

    states = np.dot(H, G_stable.initial_states)
    inputs = G_stable.inputs

    G_r = LinearSystem(A_r, B_r, C_r, inputs, states)
    return G_r

def solveLyapunovEquations(A, C):
    lambda_min = min(- np.real(linalg.eig(A)))
    A_identity = np.identity(np.size(A))
    lamba_min_matrix = np.dot(lambda_min, A_identity)

    CC= np.dot(np.transpose(C), C)
    Q = (np.transpose(A) + np.dot(lamba_min_matrix, CC)) + np.dot(CC, (A + lamba_min_matrix))
    eig_vals, right_eig_vecs = linalg.eig(Q, right = True)
    diag_eig_vals = np.diag(eig_vals)
    D = np.diag(np.dot((np.diag(diag_eig_vals)>0), np.diag(diag_eig_vals)))
    Q = np.dot(np.dot(right_eig_vecs, D), np.transpose(right_eig_vecs))
    M = CC + linalg.solve_continuous_lyapunov(np.transpose(A) + lamba_min_matrix, Q)

    return M

def calculateSurjectiveMap(m: int, k: int, n_unstable: int, G: LinearSystem):
    #  Hs is such that the eigenvalues of the matrix Hs * As,1 * Hs+ have all a strictly negative real part
    print("m")
    print(m)
    print("k")
    print(k)
    print("n_unstable")
    print(n_unstable)
    zero_matrix = np.zeros((k-n_unstable, n_unstable))
    print("np.shape(zero_matrix)")
    print(np.shape(zero_matrix))
    identity_matrix_m = np.eye(n_unstable, m)
    print("np.shape(identity_matrix_m)")
    print(np.shape(identity_matrix_m))
    identity_matrix_k= np.eye(k-n_unstable, m-n_unstable)
    print("np.shape(identity_matrix_k)")
    print(np.shape(identity_matrix_k))
    H: np.ndarray = np.eye(np.shape(identity_matrix_m)[0], np.shape(identity_matrix_k)[0])
    print("np.shape(H)")
    print(np.shape(H))
    I= H.dot(G.A).dot(linalg.pinv(H))
    print("I")
    print(linalg.eig(I)[0])
    
    return H
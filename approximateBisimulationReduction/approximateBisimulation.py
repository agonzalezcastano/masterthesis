import numpy as np
import scipy.linalg as linalg
import linearSystem
from linearSystem import LinearSystem
import accuracy

def algorithm(A, B, C, D, inputs, initial_output, initial_states, reduced_order, states_max, delta_max, error_tolerance):
    states = initial_states
    G_1 = LinearSystem(A, B, C, D, inputs, states)
    
    eig_vals, eig_vec = linalg.eig(G_1.A)
    n = np.shape(G_1.A)[0]
    n_unstable = sum(eig_vals >= 0)

    H, H_inv = calculateSurjectiveMap(n, reduced_order, n_unstable, G_1)
    G_r_2: LinearSystem = reduction(G_1, H, H_inv, reduced_order)
    states_r = linearSystem.solveLinearSystem(G_r_2)

    while  accuracy.isAccuracyCriterionSatisfied(states_r, states_max):
        if accuracy.isErrorBoundSatisfied(initial_output, G_r_2.C, G_r_2.D, G_r_2.inputs, states_r, delta_max, error_tolerance):
            eig_vals, eig_vec = linalg.eig(G_r_2.A)
            n_unstable = sum(eig_vals >= 0)
            return G_r_2.A, G_r_2.B, G_r_2.C, G_r_2.D, states_r, reduced_order
        else:
            reduced_order = reduced_order + 1
            eig_vals, eig_vec = linalg.eig(G_1.A)
            n = np.shape(G_1.A)[0]
            n_unstable = sum(eig_vals >= 0)
            H, H_inv = calculateSurjectiveMap(n, reduced_order, n_unstable, G_1)
            G_r_2: LinearSystem = reduction(G_1, H, H_inv, reduced_order)
            states_r = linearSystem.solveLinearSystem(G_r_2)


def reduction(G: LinearSystem, T, T_inv, k):
    A_r = T @ G.A @ T_inv
    B_r = T @ G.B
    C_r = G.C @ T_inv
    D_r = G.D

    eig_vals, eig_vec = linalg.eig(A_r)
    n_unstable = sum(np.real(eig_vals) >= 0)
    print("n_unstable Ar")
    print(n_unstable)

    G_r = LinearSystem(A_r, B_r, C_r, D_r, G.inputs, G.initial_states)
    return G_r

def calculateSurjectiveMap(m: int, k: int, n_unstable: int, G: LinearSystem):
    #  Hs is such that the eigenvalues of the matrix Hs * As,1 * Hs+ have all a strictly negative real part
    A = eliminateSmallValuesFromMatrix(G.A)

    trasC = np.transpose(G.C)
    T_C = trasC @ G.C
    trasA = np.transpose(A)
    trasB = np.transpose(G.B)
    T_B = G.B @ trasB

    Q = linalg.solve_continuous_lyapunov(trasA, -T_C)
    P = linalg.solve_continuous_lyapunov(A, -T_B)

    Q = nearestPD(Q)
    P = nearestPD(P)
    R = linalg.cholesky(P)
    S = linalg.cholesky(Q)

    U, s, V = linalg.svd(S @ np.transpose(R), lapack_driver='gesvd')
    HSV = s
    for i in range(0, np.shape(HSV)[0], 1):
        HSV[i] = 1/np.sqrt(HSV[i])
        if HSV[i] > 0:
            HSV[i] = -HSV[i]
    HSV = np.sort(HSV)
    HSV = np.flip(HSV)
    HSV = linalg.diagsvd(HSV, np.shape(HSV)[0], np.shape(HSV)[0])

    V_T = np.transpose(V)
    S_T = np.transpose(S)

    T = HSV @ V_T @ R
    T_inv = S_T @ U @ HSV
    T = T[:k, :]
    T_inv = T_inv[:, :k]

    return T, T_inv

def eliminateSmallValuesFromMatrix(A):
    A[np.absolute(A) < 0.000001] = 0
    return A

def nearestPD(A):
    B = (A + np.transpose(A)) / 2
    U, s, V = linalg.svd(B)

    H = np.dot(np.transpose(V), (np.diag(s) @ V))

    A2 = (B + H) / 2

    A3 = (A2 + np.transpose(A2)) / 2

    if isPD(A3):
        return A3
    spacing = np.spacing(linalg.norm(A))
    I = np.eye(np.shape(A)[0])
    k = 1
    while not isPD(A3):
        mineig = np.min(np.real(linalg.eigvals(A3)))
        A3 += I * (-mineig * k**2 + spacing)
        k += 1

    return A3

def isPD(B):
    # Returns true when input is positive-definite, via Cholesky
    try:
        _ = linalg.cholesky(B)
        return True
    except linalg.LinAlgError:
        return False
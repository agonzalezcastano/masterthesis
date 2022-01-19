
import numpy as np
from linearSystem import LinearSystem
import scipy.linalg as linalg

def decomposition(G_1: LinearSystem):
    # Decomposition of the linear system G_1 into two subsystems, respectively, stable and unstable using, first, the Schur decomposition,
    # then, solves a general form of Lyapunov equation and, with the solution, computes the second transformation.
    # G_1 = | A_s B_s | + | A_u B_u |
    #       | C_s D_s |   | C_u D_u |
    #
    # G_2 = | A_s B_s |
    #       | C_s D_s |

    eig_vals, eig_vect = linalg.eig(G_1.A)
    n = np.shape(G_1.A)[0]
    n_stable = sum(eig_vals < 0)
    n_unstable = n - n_stable

    if all(eig_vals < 0):
        G_2 = G_1
        projection = np.identity(np.shape(G_1.A)[0]) # projection is a projection matrix
    else:
        A_t, U = linalg.schur(G_1.A, output='complex')
        A_t_11 = A_t[:n_stable, :n_stable]
        A_t_12 = A_t[n_stable:, :n_stable]
        A_t_22 = A_t[n_stable:, n_stable:]

        B_t = np.dot(np.transpose(U), G_1.B)
        C_t = np.dot(G_1.C, U)

        S = linalg.solve_sylvester(A_t_11, -A_t_22, -np.transpose(A_t_12))
        I_n_stable = np.identity(n_stable)
        I_n_unstable = np.identity(n_unstable)

        W = np.block([[I_n_stable, S],[np.zeros((n_unstable, n_stable)),I_n_unstable]])
        W_inv = np.block([[I_n_stable, -S],[np.zeros((n_unstable, n_stable)),I_n_unstable]])

        A_d = np.dot(np.dot(W_inv, A_t), W)
        B_d = np.dot(W_inv, B_t)
        C_d = np.dot(C_t, W)
        D_d = G_1.D
        states_d = np.dot(W_inv, G_1.initial_states)

        A_s = A_d[:n_stable, :n_stable]
        B_s = B_d[:n_stable, :]
        C_s = C_d[:, :n_stable]
        D_s = D_d
        states_s = states_d[:n_stable, :]

        projection = np.identity(np.shape(A_s)[0])
        #eigvals_2 = linalg.eig(A_s)[0]
        #projection = projection * eigvals_2
        #states_s = np.dot(projection, states_s)

        G_2 = LinearSystem(A_s, B_s, C_s, D_s, G_1.inputs, states_s)

    return G_2, projection
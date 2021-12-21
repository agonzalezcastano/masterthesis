
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

    n = np.size(G_1.A) 
    n_stable = sum(linalg.eig(G_1.A) < 0)
    n_unstable = n - n_stable

    if all(linalg.eig(G_1.A)<0):
        G_2 = G_1
        projection = np.identity(np.size(G_1.A)) # projection is a projection matrix
    else:
        A_t, U = linalg.schur(G_1.A, output='complex')
        A_t_11 = A_t[:n_stable, :n_stable]
        A_t_12 = A_t[n_stable:, :n_stable]
        A_t_22 = A_t[n_stable:, n_stable:]

        B_t = np.dot(np.transpose(U), G_1.B)
        C_t = np.dot(G_1.C, U)

        S = linalg.solve_sylvester(A_t_11, -A_t_22, -A_t_12)
        I_n_stable = np.identity(n_stable)
        I_n_unstable = np.identity(n_unstable)

        W = np.array([[I_n_stable, S], 
                        [np.zeros((n_stable, n_unstable)), I_n_unstable]])
        W_inv = np.array([[I_n_stable, -S],
                        [np.zeros((n_stable, n_unstable)), I_n_unstable]])

        A_d = np.dot(np.dot(W_inv, A_t), W)
        B_d = np.dot(W_inv, B_t)
        C_d = np.dot(C_t, W)

        A_s = A_d[:n_stable, :n_stable]
        B_s = B_d[:, :n_stable]
        C_s = C_d[:n_stable, :]

        projection = np.identity(np.size(A_s))
        eigvals_1 = linalg.eig(G_1.A)
        eigvals_2 = linalg.eig(A_s)
        projection = np.dot(eigvals_2, linalg.inv(eigvals_1))
        inputs_s = G_1.inputs
        initial_states_s = np.dot(projection, G_1.initial_states)

        G_2 = LinearSystem(A_s, B_s, C_s, inputs_s, initial_states_s)

    return G_2, projection
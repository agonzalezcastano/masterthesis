import projectionMatrix
import reducedSystem
import interpolationPoints
import numpy.linalg as linalg
import scipy.linalg as la
import numpy as np

def algorithm(A, B, C, D, inputs, initial_states, n_inter_points, error_tolerance, reduced_order):
    A, B, C, D, inputs, initial_states = extractStableSystem(A, B, C, D, inputs, initial_states, reduced_order)
    init_sigma = interpolationPoints.calculateInitialInterpolationPoints(A, n_inter_points)
    V = projectionMatrix.calculateProjectionMatrixV(A, B, init_sigma)
    Q = projectionMatrix.calculateProjectionMatrixQ(A, C)
    Z = projectionMatrix.calculateProjectionMatrixZ(Q, V)
    A_r, B_r, C_r, D_r = reducedSystem.computeReducedSystem(A, B, C, D, Z, V)
    
    k = 0
    condition = (np.real(init_sigma[k + 1]) - np.real(init_sigma[k]))/np.real(init_sigma[k])
    
    while np.absolute(condition) >= error_tolerance:
        eigen_vals, eigen_vec = linalg.eig(A_r)
        sigma = interpolationPoints.calculateInterpolationPoints(eigen_vals, n_inter_points)
        V = projectionMatrix.calculateProjectionMatrixV(A_r, B_r, sigma)
        Q = projectionMatrix.calculateProjectionMatrixQ(A_r, C_r)
        Z = projectionMatrix.calculateProjectionMatrixZ(Q, V)
        A_r, B_r, C_r, D_r = reducedSystem.computeReducedSystem(A_r, B_r, C_r, D_r, Z, V)
        k = k + 1
        condition = (np.real(sigma[k + 1]) - np.real(sigma[k]))/np.real(sigma[k])

    # solve linear system to obtain the reduced states
    states_r = np.dot(linalg.pinv(-A_r), np.dot(B_r, inputs))

    return A_r, B_r, C_r, D_r, states_r

def extractStableSystem(A, B, C, D, inputs, initial_states, reduced_order):
    eig_vals, eig_vec = linalg.eig(A)
    n_unstable = sum(eig_vals >= 0)

    if n_unstable > reduced_order:
        print('Dimension of the reduced-order model must be greater than the dimension of the unstable subsystem of G')
        print('Dimension of the unstable system is: ')
        print(n_unstable)
    if n_unstable <= reduced_order:
        # System is unstable
        # Extraction of the stable subsystem
        A_stable, B_stable, C_stable, D_stable, inputs, initial_states_stable = decomposition(A, B, C, D, inputs, initial_states)
    if n_unstable == 0:
        # System is stable
        A_stable = A
        B_stable = B
        C_stable = C
        D_stable = D
        initial_states_stable = initial_states

    return A_stable, B_stable, C_stable, D_stable, inputs, initial_states_stable

def decomposition(A, B, C, D, inputs, initial_states):
    # Decomposition of the linear system G_1 into two subsystems, respectively, stable and unstable using, first, the Schur decomposition,
    # then, solves a general form of Lyapunov equation and, with the solution, computes the second transformation.
    # G_1 = | A_s B_s | + | A_u B_u |
    #       | C_s D_s |   | C_u D_u |
    #
    # G_2 = | A_s B_s |
    #       | C_s D_s |

    eig_vals, eig_vect = linalg.eig(A)
    n = np.shape(A)[0]
    n_stable = sum(eig_vals < 0)
    n_unstable = n - n_stable

    if all(eig_vals < 0):
        A_s = A
        B_s = B
        C_s = C
        D_s = D
        inputs = inputs
        states_s = initial_states

    else:
        A_t, U = la.schur(A, output='complex')
        A_t_11 = A_t[:n_stable, :n_stable]
        A_t_12 = A_t[n_stable:, :n_stable]
        A_t_22 = A_t[n_stable:, n_stable:]

        B_t = np.dot(np.transpose(U), B)
        C_t = np.dot(C, U)

        S = la.solve_sylvester(A_t_11, -A_t_22, -np.transpose(A_t_12))
        I_n_stable = np.identity(n_stable)
        I_n_unstable = np.identity(n_unstable)

        W = np.block([[I_n_stable, S],[np.zeros((n_unstable, n_stable)),I_n_unstable]])
        W_inv = np.block([[I_n_stable, -S],[np.zeros((n_unstable, n_stable)),I_n_unstable]])

        A_d = np.dot(np.dot(W_inv, A_t), W)
        B_d = np.dot(W_inv, B_t)
        C_d = np.dot(C_t, W)
        D_d = D
        states_d = np.dot(W_inv, initial_states)

        A_s = A_d[:n_stable, :n_stable]
        B_s = B_d[:n_stable, :]
        C_s = C_d[:, :n_stable]
        D_s = D_d
        states_s = states_d[:n_stable, :]

    return A_s, B_s, C_s, D_s, inputs, states_s
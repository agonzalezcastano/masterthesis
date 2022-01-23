import projectionMatrix
import reducedSystem
import interpolationPoints
import numpy.linalg as linalg
import numpy as np

def algorithm(A, B, C, D, inputs, n_inter_points, error_tolerance):
    init_sigma = interpolationPoints.calculateInitialInterpolationPoints(A, n_inter_points)
    V = projectionMatrix.calculateProjectionMatrixV(A, B, init_sigma)
    Q = projectionMatrix.calculateProjectionMatrixQ(A, C)
    Z = projectionMatrix.calculateProjectionMatrixZ(Q, V)
    A_r, B_r, C_r, D_r = reducedSystem.computeReducedSystem(A, B, C, D, Z, V)
    
    k = 0
    condition = (np.real(init_sigma[k + 1]) - np.real(init_sigma[k]))/np.real(init_sigma[k])
    
    while np.absolute(condition) >= error_tolerance:
        eigen_vals, eigen_vec = linalg.eig(A_r)
        reduced_eigen_values = np.diag(-eigen_vals)
        sigma = interpolationPoints.calculateInterpolationPoints(reduced_eigen_values, n_inter_points)
        V = projectionMatrix.calculateProjectionMatrixV(A_r, B_r, sigma)
        Q = projectionMatrix.calculateProjectionMatrixQ(A_r, C_r)
        Z = projectionMatrix.calculateProjectionMatrixZ(Q, V)
        A_r, B_r, C_r, D_r = reducedSystem.computeReducedSystem(A_r, B_r, C_r, D_r, Z, V)
        k = k + 1
        condition = (np.real(sigma[k + 1]) - np.real(sigma[k]))/np.real(sigma[k])

    # solve linear system to obtain the reduced states
    states_r = -np.dot(linalg.pinv(A_r), np.dot(B_r, inputs))
    states_r = np.imag(states_r)

    return A_r, B_r, C_r, D_r, states_r
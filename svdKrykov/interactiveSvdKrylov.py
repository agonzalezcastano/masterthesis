import projectionMatrix
import reducedSystem
import reducedMatrix
import interpolationPoints
import numpy.linalg as linalg
import numpy as np

def algorithm(A, B, C, D, n_inter_points, error_tolerance):
    init_sigma = interpolationPoints.calculateInitialInterpolationPoints(A, n_inter_points)
    V = projectionMatrix.calculateProjectionMatrixV(A, B, init_sigma)
    Q = projectionMatrix.calculateProjectionMatrixQ(A, C)
    Z = projectionMatrix.calculateProjectionMatrixZ(Q, V)
    A_r = reducedMatrix.computeReducedMatrixA(A, Z, V)
    
    k = 0
    condition = abs((init_sigma.real[k + 1] - init_sigma.real[k])/init_sigma.real[k])
    
    while condition >= error_tolerance:
        print("k")
        print(k)
        eigen_vals, eigen_vec = linalg.eig(A_r)
        reduced_eigen_values = np.diag(-eigen_vals)
        print("shape reduced_eigen_values")
        print(np.shape(reduced_eigen_values))
        sigma = interpolationPoints.calculateInterpolationPoints(reduced_eigen_values)
        V = projectionMatrix.calculateProjectionMatrixV(A_r, B, sigma)
        Z = projectionMatrix.calculateProjectionMatrixZ(Q, V)
        A_r = reducedMatrix.computeReducedMatrixA(A_r, Z, V)
        condition = (sigma[k + 1] - sigma[k])/sigma[k]
        k = k + 1

    A_r, B_r, C_r, D_r = reducedSystem.computeReducedSystem(A, B, C, D, Z, V)
    return A_r, B_r, C_r, D_r
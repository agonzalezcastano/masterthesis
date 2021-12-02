import eigenValues
import projectionMatrix
import reducedSystem
import reducedMatrix
import interpolationPoints

def algorithm(A, B, C, D, k, t, error_tolerance):
    init_eigen_values = eigenValues.calculateInitialEigenvalues(A, k)
    V = projectionMatrix.calculateProjectionMatrixV(A, B, init_eigen_values)
    Q = projectionMatrix.calculateProjectionMatrixQ(A, C)
    Z = projectionMatrix.calculateProjectionMatrixZ(Q, V)
    
    condition = ((init_eigen_values + 1) - init_eigen_values)/init_eigen_values
    
    while condition >= error_tolerance:
        A_r = reducedMatrix.computeReducedMatrixA(A, Z, V)
        reduced_eigen_values = eigenValues.calculateEigenvalues(A_r)
        int_points = interpolationPoints.calculateInterpolationPoints(reduced_eigen_values)
        V = projectionMatrix.calculateProjectionMatrixV(A, B, int_points)
        Z = projectionMatrix.calculateProjectionMatrixZ(Q, V)
        condition = ((init_eigen_values + 1) - init_eigen_values)/init_eigen_values

    Gr = reducedSystem.createReducedSystem(A, B, C, D, Z, V)
    return Gr
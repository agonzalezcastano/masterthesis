import numpy.linalg as linalg
import numpy.random as rand
import numpy as np

def calculateInitialInterpolationPoints(A, n_int_points):
    eigen_values, eigen_vect = linalg.eig(A)
    real = eigen_values.real
    imag = eigen_values.imag
    
    min_real = min(real)
    max_real = max(real)
    min_imag = min(imag)
    max_imag = max(imag)
    
    int_points = np.empty(0)
    for num in range(0, n_int_points, 1):
        eigen_value_reduced_real = rand.uniform(min_real, max_real)
        eigen_value_reduced_imag = rand.uniform(min_imag, max_imag)
        int_points = np.append(int_points, complex(eigen_value_reduced_real,eigen_value_reduced_imag))

    return int_points

def calculateInterpolationPoints(eigen_values, n_int_points):
    int_points = np.empty(0)
    for num in range(0, n_int_points, 1):
        int_points = np.append(int_points, -eigen_values[num, 0])

    return int_points
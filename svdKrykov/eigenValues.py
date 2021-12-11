import numpy.linalg as linalg
import numpy as np

def calculateEigenvalues(A):
    eigen_values = linalg.eig(A)
    return eigen_values

def calculateInitialEigenvalues(A, k):
    eigen_values = calculateEigenvalues(A)
    real = np.real(eigen_values)
    imag = np.imag(eigen_values)
    
    min_real = min(real)
    max_real = max(real)
    min_imag = min(imag)
    max_imag = max(imag)
    
    eigen_values_reduced = []
    for num in range(0, k+1, 1):
        eigen_value_reduced_real = linalg.random.uniform(min_real, max_real)
        eigen_value_reduced_imag = linalg.random.uniform(min_imag, max_imag)
        eigen_values_reduced = linalg.append(complex(eigen_value_reduced_real,eigen_value_reduced_imag))
    
    return eigen_values_reduced
import numpy.linalg as linalg

def calculateEigenvalues(A):
    eigen_values = linalg.eig(A)
    return eigen_values

def calculateInitialEigenvalues(A, k):
    eigen_values = calculateEigenvalues(A)
    real = eigen_values.real
    imag = eigen_values.imag
    
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
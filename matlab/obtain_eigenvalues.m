%First, the file struct_ieee34 and/or struct_ieee34_part must be uploaded to
%matlab.
% Both of these files contain a variable called test, from where the
% part of the information is extracted.
% Also is necessary to have previously executed the obtain_reduced_state_space_matrices.m file
% as part of the information is extracted from the variables created with it.

eigA = eig(test.A);
plot(real(eigA),imag(eigA),'ko')
title('Eigenvalues of the system')
xlabel('Real')
ylabel('Imaginary')

eigA_svd = eig(A_var_svdkrylov);
hold on
plot(real(eigA_svd),imag(eigA_svd),'bx')
title('Eigenvalues of the original system vs. Eigenvalues of the SVD-Krylov Reduced System')
xlabel('Real')
ylabel('Imaginary')

eigA_approx = eig(A_var_approx_bisimulation);
hold on
plot(real(eigA_approx),imag(eigA_approx),'mx')
title('Eigenvalues of the original system vs. Eigenvalues of the Approximation Bisimulation Reduced System')
xlabel('Real')
ylabel('Imaginary')

eigA_spectral = eig(A_var_spectral_projection);
hold on
plot(real(eigA_spectral),imag(eigA_spectral),'rx')
title('Eigenvalues of the original system vs. Eigenvalues of the Spectral Projection Reduced System')
xlabel('Real')
ylabel('Imaginary')

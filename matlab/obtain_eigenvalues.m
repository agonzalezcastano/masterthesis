%First, the file struct_ieee34 and/or struct_ieee34_part must be uploaded to
%matlab.
% Both of these files contain a variable called test, from where the
% part of the information is extracted.
% Also is necessary to have previously executed the obtain_reduced_state_space_matrices.m file
% as part of the information is extracted from the variables created with it.

eigA = eig(test.A);

subplot(1,2,1)
plot(real(eigA),imag(eigA),'ko')
title('Eigenvalues of the original system')
xlabel('Real')
ylabel('Imaginary')

eigA_spectral = eig(A_var_spectral_projection);
subplot(1,2,2)
%hold on
plot(real(eigA_spectral),imag(eigA_spectral),'rx')
%title('Eigenvalues of the original system vs. Eigenvalues of the Spectral Projection Reduced System')
%xlabel('Real')
%ylabel('Imaginary')

eigA_svd = eig(A_var_svdkrylov);
%subplot(1,2,2)
%plot(real(eigA),imag(eigA),'ko')
hold on
plot(real(eigA_svd),imag(eigA_svd),'kx')
%title('Eigenvalues of the original system vs. Eigenvalues of the SVD-Krylov Reduced System')
%xlabel('Real')
%ylabel('Imaginary')

eigA_approx = eig(A_var_approx_bisimulation);
%subplot(1,2,2)
%plot(real(eigA),imag(eigA),'ko')
hold on
plot(real(eigA_approx),imag(eigA_approx),'bx')
title('Reduced Eigenvalues')
%title('Eigenvalues of the original system vs. Eigenvalues of the Approximation Bisimulation Reduced System')
xlabel('Real')
ylabel('Imaginary')
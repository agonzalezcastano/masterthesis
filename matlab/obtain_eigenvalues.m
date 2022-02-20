%First, the file struct_ieee34 and/or struct_ieee34_part must be uploaded to
%matlab.
% Both of these files contain a variable called test, from where the
% part of the information is extracted.
% Also is necessary to have previously executed the obtain_reduced_state_space_matrices.m file
% as part of the information is extracted from the variables created with it.

eigA = eig(A);

subplot(1,2,1)
plot(real(eigA),imag(eigA),'ko')
title('Original Eigenvalues')
xlabel('Real')
ylabel('Imaginary')
xlim([-6e7 3e7])
ylim([-4e04 4e04])

eigA_spectral = eig(A_spectral_projection);
subplot(1,2,2)
plot(real(eigA_spectral),imag(eigA_spectral),'rx')

eigA_svd = eig(A_svdkrylov);
hold on
plot(real(eigA_svd),imag(eigA_svd),'kx')

eigA_approx = eig(A_approx_bisimulation);
hold on
plot(real(eigA_approx),imag(eigA_approx),'bx')
title('Reduced Eigenvalues')
xlabel('Real')
xlim([-6e7 3e7])
ylim([-4e04 4e04])
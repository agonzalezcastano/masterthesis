% After the execution of the three algorithm, this file saves the state-space matices obtained
% into Matlab.
% Depending on the system reduced, one should use eigther part_system_data or whole_system_data
path = '/Users/amparogonzalezcastano/Documents/GitHub/masterthesis/results/';

part_system_data = 'ieee34_reduced_part_';
whole_system_data = 'ieee34_reduced_';

A_var_spectral_projection = readtable(strcat(path,strcat(whole_system_data,'A_spectralProjection.csv')));
B_var_spectral_projection = readtable(strcat(path,strcat(whole_system_data,'B_spectralProjection.csv')));
C_var_spectral_projection = readtable(strcat(path,strcat(whole_system_data,'C_spectralProjection.csv')));
D_var_spectral_projection = readtable(strcat(path,strcat(whole_system_data,'D_spectralProjection.csv')));
states_var_spectral_projection = readtable(strcat(path,strcat(whole_system_data,'states_spectralProjection.csv')));

A_var_svdkrylov = readtable(strcat(path,strcat(whole_system_data,'A_svdKrylov.csv')));
B_var_svdkrylov = readtable(strcat(path,strcat(whole_system_data,'B_svdKrylov.csv')));
C_var_svdkrylov = readtable(strcat(path,strcat(whole_system_data,'C_svdKrylov.csv')));
D_var_svdkrylov = readtable(strcat(path,strcat(whole_system_data,'D_svdKrylov.csv')));
states_var_svdkrylov = readtable(strcat(path,strcat(whole_system_data,'states_svdKrylov.csv')));

A_var_approx_bisimulation = readtable(strcat(path,strcat(whole_system_data,'A_approximateBisimulation.csv')));
B_var_approx_bisimulation = readtable(strcat(path,strcat(whole_system_data,'B_approximateBisimulation.csv')));
C_var_approx_bisimulation = readtable(strcat(path,strcat(whole_system_data,'C_approximateBisimulation.csv')));
D_var_approx_bisimulation = readtable(strcat(path,strcat(whole_system_data,'D_approximateBisimulation.csv')));
states_var_approx_bisimulation = readtable(strcat(path,strcat(whole_system_data,'states_approximateBisimulation.csv')));

A_var_spectral_projection = table2array(A_var_spectral_projection);
B_var_spectral_projection = table2array(B_var_spectral_projection);
C_var_spectral_projection = table2array(C_var_spectral_projection);
D_var_spectral_projection = table2array(D_var_spectral_projection);
states_var_spectral_projection = table2array(states_var_spectral_projection);

A_var_svdkrylov = table2array(A_var_svdkrylov);
B_var_svdkrylov = table2array(B_var_svdkrylov);
C_var_svdkrylov = table2array(C_var_svdkrylov);
D_var_svdkrylov = table2array(D_var_svdkrylov);
states_var_svdkrylov = table2array(states_var_svdkrylov);

A_var_approx_bisimulation = table2array(A_var_approx_bisimulation);
B_var_approx_bisimulation = table2array(B_var_approx_bisimulation);
C_var_approx_bisimulation = table2array(C_var_approx_bisimulation);
D_var_approx_bisimulation = table2array(D_var_approx_bisimulation);
states_var_approx_bisimulation = table2array(states_var_approx_bisimulation);

% After the execution of the three algorithm, this file saves the state-space matices obtained
% into Matlab.
% Depending on the system reduced, one should use eigther ieee34_part_system_data or ieee34_part_system_data
path = '/Users/amparogonzalezcastano/Documents/GitHub/masterthesis/results/';

ieee34_part_system_data = 'ieee34_reduced_part_';
ieee34_system_data = 'ieee34_reduced_';
ieee123_system_data = 'ieee123_reduced_';

% A_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'A_spectralProjection.csv')));
% B_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'B_spectralProjection.csv')));
% C_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'C_spectralProjection.csv')));
% D_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'D_spectralProjection.csv')));
% states_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'states_spectralProjection.csv')));
% initial_states_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'initial_states_spectralProjection.csv')));
% output_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'output_spectralProjection.csv')));
% 
% A_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'A_svdKrylov.csv')));
% B_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'B_svdKrylov.csv')));
% C_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'C_svdKrylov.csv')));
% D_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'D_svdKrylov.csv')));
% states_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'states_svdKrylov.csv')));
% initial_states_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'initial_states_svdKrylov.csv')));
% output_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'output_svdKrylov.csv')));

A_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'A_approximateBisimulation.csv')));
B_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'B_approximateBisimulation.csv')));
C_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'C_approximateBisimulation.csv')));
D_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'D_approximateBisimulation.csv')));
initial_states_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'initial_states_approximateBisimulation.csv')));
states_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'states_approximateBisimulation.csv')));
output_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'output_approximateBisimulation.csv')));

% A_spectral_projection = table2array(A_spectral_projection);
% B_spectral_projection = table2array(B_spectral_projection);
% C_spectral_projection = table2array(C_spectral_projection);
% D_spectral_projection = table2array(D_spectral_projection);
% states_spectral_projection = table2array(states_spectral_projection);
% initial_states_spectral_projection = table2array(initial_states_spectral_projection);
% output_spectral_projection = table2array(output_spectral_projection);

% A_svdkrylov = table2array(A_svdkrylov);
% B_svdkrylov = table2array(B_svdkrylov);
% C_svdkrylov = table2array(C_svdkrylov);
% D_svdkrylov = table2array(D_svdkrylov);
% states_svdkrylov = table2array(states_svdkrylov);
% initial_states_svdkrylov = table2array(initial_states_svdkrylov);
% output_svdkrylov = table2array(output_svdkrylov);

A_approx_bisimulation = table2array(A_approx_bisimulation);
B_approx_bisimulation = table2array(B_approx_bisimulation);
C_approx_bisimulation = table2array(C_approx_bisimulation);
D_approx_bisimulation = table2array(D_approx_bisimulation);
states_approx_bisimulation = table2array(states_approx_bisimulation);
initial_states_approx_bisimulation = table2array(initial_states_approx_bisimulation);
output_approx_bisimulation = table2array(output_approx_bisimulation);

% After the execution of the three algorithm, this file saves the state-space matices obtained
% into Matlab.

path = '/Users/amparogonzalezcastano/Documents/GitHub/masterthesis/results/';

ieee34_system_data = 'ieee34_reduced_';

ieee34_A_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'A_spectralProjection.csv')));
ieee34_B_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'B_spectralProjection.csv')));
ieee34_C_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'C_spectralProjection.csv')));
ieee34_D_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'D_spectralProjection.csv')));
ieee34_states_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'states_spectralProjection.csv')));
ieee34_initial_states_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'initial_states_spectralProjection.csv')));
ieee34_output_spectral_projection = readtable(strcat(path,strcat(ieee34_system_data,'output_spectralProjection.csv')));

ieee34_A_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'A_svdKrylov.csv')));
ieee34_B_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'B_svdKrylov.csv')));
ieee34_C_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'C_svdKrylov.csv')));
ieee34_D_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'D_svdKrylov.csv')));
ieee34_states_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'states_svdKrylov.csv')));
ieee34_initial_states_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'initial_states_svdKrylov.csv')));
ieee34_output_svdkrylov = readtable(strcat(path,strcat(ieee34_system_data,'output_svdKrylov.csv')));

ieee34_A_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'A_approximateBisimulation.csv')));
ieee34_B_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'B_approximateBisimulation.csv')));
ieee34_C_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'C_approximateBisimulation.csv')));
ieee34_D_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'D_approximateBisimulation.csv')));
ieee34_initial_states_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'initial_states_approximateBisimulation.csv')));
ieee34_states_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'states_approximateBisimulation.csv')));
ieee34_output_approx_bisimulation = readtable(strcat(path,strcat(ieee34_system_data,'output_approximateBisimulation.csv')));

ieee34_A_spectral_projection = table2array(ieee34_A_spectral_projection);
ieee34_B_spectral_projection = table2array(ieee34_B_spectral_projection);
ieee34_C_spectral_projection = table2array(ieee34_C_spectral_projection);
ieee34_D_spectral_projection = table2array(ieee34_D_spectral_projection);
ieee34_states_spectral_projection = table2array(ieee34_states_spectral_projection);
ieee34_initial_states_spectral_projection = table2array(ieee34_initial_states_spectral_projection);
ieee34_output_spectral_projection = table2array(ieee34_output_spectral_projection);

ieee34_A_svdkrylov = table2array(ieee34_A_svdkrylov);
ieee34_B_svdkrylov = table2array(ieee34_B_svdkrylov);
ieee34_C_svdkrylov = table2array(ieee34_C_svdkrylov);
ieee34_D_svdkrylov = table2array(ieee34_D_svdkrylov);
ieee34_states_svdkrylov = table2array(ieee34_states_svdkrylov);
ieee34_initial_states_svdkrylov = table2array(ieee34_initial_states_svdkrylov);
ieee34_output_svdkrylov = table2array(ieee34_output_svdkrylov);

ieee34_A_approx_bisimulation = table2array(ieee34_A_approx_bisimulation);
ieee34_B_approx_bisimulation = table2array(ieee34_B_approx_bisimulation);
ieee34_C_approx_bisimulation = table2array(ieee34_C_approx_bisimulation);
ieee34_D_approx_bisimulation = table2array(ieee34_D_approx_bisimulation);
ieee34_states_approx_bisimulation = table2array(ieee34_states_approx_bisimulation);
ieee34_initial_states_approx_bisimulation = table2array(ieee34_initial_states_approx_bisimulation);
ieee34_output_approx_bisimulation = table2array(ieee34_output_approx_bisimulation);

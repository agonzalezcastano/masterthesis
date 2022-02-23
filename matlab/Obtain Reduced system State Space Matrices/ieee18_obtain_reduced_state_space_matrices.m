% After the execution of the three algorithm, this file saves the state-space matices obtained
% into Matlab.

path = '/Users/amparogonzalezcastano/Documents/GitHub/masterthesis/results/';

ieee18_system_data = 'ieee18_reduced_';

ieee18_A_spectral_projection = readtable(strcat(path,strcat(ieee18_system_data,'A_spectralProjection.csv')));
ieee18_B_spectral_projection = readtable(strcat(path,strcat(ieee18_system_data,'B_spectralProjection.csv')));
ieee18_C_spectral_projection = readtable(strcat(path,strcat(ieee18_system_data,'C_spectralProjection.csv')));
ieee18_D_spectral_projection = readtable(strcat(path,strcat(ieee18_system_data,'D_spectralProjection.csv')));
ieee18_states_spectral_projection = readtable(strcat(path,strcat(ieee18_system_data,'states_spectralProjection.csv')));
ieee18_initial_states_spectral_projection = readtable(strcat(path,strcat(ieee18_system_data,'initial_states_spectralProjection.csv')));
ieee18_output_spectral_projection = readtable(strcat(path,strcat(ieee18_system_data,'output_spectralProjection.csv')));

ieee18_A_svdkrylov = readtable(strcat(path,strcat(ieee18_system_data,'A_svdKrylov.csv')));
ieee18_B_svdkrylov = readtable(strcat(path,strcat(ieee18_system_data,'B_svdKrylov.csv')));
ieee18_C_svdkrylov = readtable(strcat(path,strcat(ieee18_system_data,'C_svdKrylov.csv')));
ieee18_D_svdkrylov = readtable(strcat(path,strcat(ieee18_system_data,'D_svdKrylov.csv')));
ieee18_states_svdkrylov = readtable(strcat(path,strcat(ieee18_system_data,'states_svdKrylov.csv')));
ieee18_initial_states_svdkrylov = readtable(strcat(path,strcat(ieee18_system_data,'initial_states_svdKrylov.csv')));
ieee18_output_svdkrylov = readtable(strcat(path,strcat(ieee18_system_data,'output_svdKrylov.csv')));

ieee18_A_approx_bisimulation = readtable(strcat(path,strcat(ieee18_system_data,'A_approximateBisimulation.csv')));
ieee18_B_approx_bisimulation = readtable(strcat(path,strcat(ieee18_system_data,'B_approximateBisimulation.csv')));
ieee18_C_approx_bisimulation = readtable(strcat(path,strcat(ieee18_system_data,'C_approximateBisimulation.csv')));
ieee18_D_approx_bisimulation = readtable(strcat(path,strcat(ieee18_system_data,'D_approximateBisimulation.csv')));
ieee18_initial_states_approx_bisimulation = readtable(strcat(path,strcat(ieee18_system_data,'initial_states_approximateBisimulation.csv')));
ieee18_states_approx_bisimulation = readtable(strcat(path,strcat(ieee18_system_data,'states_approximateBisimulation.csv')));
ieee18_output_approx_bisimulation = readtable(strcat(path,strcat(ieee18_system_data,'output_approximateBisimulation.csv')));

ieee18_A_spectral_projection = table2array(ieee18_A_spectral_projection);
ieee18_B_spectral_projection = table2array(ieee18_B_spectral_projection);
ieee18_C_spectral_projection = table2array(ieee18_C_spectral_projection);
ieee18_D_spectral_projection = table2array(ieee18_D_spectral_projection);
ieee18_states_spectral_projection = table2array(ieee18_states_spectral_projection);
ieee18_initial_states_spectral_projection = table2array(ieee18_initial_states_spectral_projection);
ieee18_output_spectral_projection = table2array(ieee18_output_spectral_projection);

ieee18_A_svdkrylov = table2array(ieee18_A_svdkrylov);
ieee18_B_svdkrylov = table2array(ieee18_B_svdkrylov);
ieee18_C_svdkrylov = table2array(ieee18_C_svdkrylov);
ieee18_D_svdkrylov = table2array(ieee18_D_svdkrylov);
ieee18_states_svdkrylov = table2array(ieee18_states_svdkrylov);
ieee18_initial_states_svdkrylov = table2array(ieee18_initial_states_svdkrylov);
ieee18_output_svdkrylov = table2array(ieee18_output_svdkrylov);

ieee18_A_approx_bisimulation = table2array(ieee18_A_approx_bisimulation);
ieee18_B_approx_bisimulation = table2array(ieee18_B_approx_bisimulation);
ieee18_C_approx_bisimulation = table2array(ieee18_C_approx_bisimulation);
ieee18_D_approx_bisimulation = table2array(ieee18_D_approx_bisimulation);
ieee18_states_approx_bisimulation = table2array(ieee18_states_approx_bisimulation);
ieee18_initial_states_approx_bisimulation = table2array(ieee18_initial_states_approx_bisimulation);
ieee18_output_approx_bisimulation = table2array(ieee18_output_approx_bisimulation);

% After the execution of the three algorithm, this file saves the state-space matices obtained
% into Matlab.

path = '/Users/amparogonzalezcastano/Documents/GitHub/masterthesis/results/';

ieee7_system_data = 'ieee7_reduced_';

ieee7_A_spectral_projection = readtable(strcat(path,strcat(ieee7_system_data,'A_spectralProjection.csv')));
ieee7_B_spectral_projection = readtable(strcat(path,strcat(ieee7_system_data,'B_spectralProjection.csv')));
ieee7_C_spectral_projection = readtable(strcat(path,strcat(ieee7_system_data,'C_spectralProjection.csv')));
ieee7_D_spectral_projection = readtable(strcat(path,strcat(ieee7_system_data,'D_spectralProjection.csv')));
ieee7_states_spectral_projection = readtable(strcat(path,strcat(ieee7_system_data,'states_spectralProjection.csv')));
ieee7_initial_states_spectral_projection = readtable(strcat(path,strcat(ieee7_system_data,'initial_states_spectralProjection.csv')));
ieee7_output_spectral_projection = readtable(strcat(path,strcat(ieee7_system_data,'output_spectralProjection.csv')));

ieee7_A_svdkrylov = readtable(strcat(path,strcat(ieee7_system_data,'A_svdKrylov.csv')));
ieee7_B_svdkrylov = readtable(strcat(path,strcat(ieee7_system_data,'B_svdKrylov.csv')));
ieee7_C_svdkrylov = readtable(strcat(path,strcat(ieee7_system_data,'C_svdKrylov.csv')));
ieee7_D_svdkrylov = readtable(strcat(path,strcat(ieee7_system_data,'D_svdKrylov.csv')));
ieee7_states_svdkrylov = readtable(strcat(path,strcat(ieee7_system_data,'states_svdKrylov.csv')));
ieee7_initial_states_svdkrylov = readtable(strcat(path,strcat(ieee7_system_data,'initial_states_svdKrylov.csv')));
ieee7_output_svdkrylov = readtable(strcat(path,strcat(ieee7_system_data,'output_svdKrylov.csv')));

ieee7_A_approx_bisimulation = readtable(strcat(path,strcat(ieee7_system_data,'A_approximateBisimulation.csv')));
ieee7_B_approx_bisimulation = readtable(strcat(path,strcat(ieee7_system_data,'B_approximateBisimulation.csv')));
ieee7_C_approx_bisimulation = readtable(strcat(path,strcat(ieee7_system_data,'C_approximateBisimulation.csv')));
ieee7_D_approx_bisimulation = readtable(strcat(path,strcat(ieee7_system_data,'D_approximateBisimulation.csv')));
ieee7_initial_states_approx_bisimulation = readtable(strcat(path,strcat(ieee7_system_data,'initial_states_approximateBisimulation.csv')));
ieee7_states_approx_bisimulation = readtable(strcat(path,strcat(ieee7_system_data,'states_approximateBisimulation.csv')));
ieee7_output_approx_bisimulation = readtable(strcat(path,strcat(ieee7_system_data,'output_approximateBisimulation.csv')));

ieee7_A_spectral_projection = table2array(ieee7_A_spectral_projection);
ieee7_B_spectral_projection = table2array(ieee7_B_spectral_projection);
ieee7_C_spectral_projection = table2array(ieee7_C_spectral_projection);
ieee7_D_spectral_projection = table2array(ieee7_D_spectral_projection);
ieee7_states_spectral_projection = table2array(ieee7_states_spectral_projection);
ieee7_initial_states_spectral_projection = table2array(ieee7_initial_states_spectral_projection);
ieee7_output_spectral_projection = table2array(ieee7_output_spectral_projection);

ieee7_A_svdkrylov = table2array(ieee7_A_svdkrylov);
ieee7_B_svdkrylov = table2array(ieee7_B_svdkrylov);
ieee7_C_svdkrylov = table2array(ieee7_C_svdkrylov);
ieee7_D_svdkrylov = table2array(ieee7_D_svdkrylov);
ieee7_states_svdkrylov = table2array(ieee7_states_svdkrylov);
ieee7_initial_states_svdkrylov = table2array(ieee7_initial_states_svdkrylov);
ieee7_output_svdkrylov = table2array(ieee7_output_svdkrylov);

ieee7_A_approx_bisimulation = table2array(ieee7_A_approx_bisimulation);
ieee7_B_approx_bisimulation = table2array(ieee7_B_approx_bisimulation);
ieee7_C_approx_bisimulation = table2array(ieee7_C_approx_bisimulation);
ieee7_D_approx_bisimulation = table2array(ieee7_D_approx_bisimulation);
ieee7_states_approx_bisimulation = table2array(ieee7_states_approx_bisimulation);
ieee7_initial_states_approx_bisimulation = table2array(ieee7_initial_states_approx_bisimulation);
ieee7_output_approx_bisimulation = table2array(ieee7_output_approx_bisimulation);

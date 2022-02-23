% After the execution of the three algorithm, this file saves the state-space matices obtained
% into Matlab.

path = '/Users/amparogonzalezcastano/Documents/GitHub/masterthesis/results/';

ieee5_system_data = 'ieee5_reduced_';

ieee5_A_spectral_projection = readtable(strcat(path,strcat(ieee5_system_data,'A_spectralProjection.csv')));
ieee5_B_spectral_projection = readtable(strcat(path,strcat(ieee5_system_data,'B_spectralProjection.csv')));
ieee5_C_spectral_projection = readtable(strcat(path,strcat(ieee5_system_data,'C_spectralProjection.csv')));
ieee5_D_spectral_projection = readtable(strcat(path,strcat(ieee5_system_data,'D_spectralProjection.csv')));
ieee5_states_spectral_projection = readtable(strcat(path,strcat(ieee5_system_data,'states_spectralProjection.csv')));
ieee5_initial_states_spectral_projection = readtable(strcat(path,strcat(ieee5_system_data,'initial_states_spectralProjection.csv')));
ieee5_output_spectral_projection = readtable(strcat(path,strcat(ieee5_system_data,'output_spectralProjection.csv')));

ieee5_A_svdkrylov = readtable(strcat(path,strcat(ieee5_system_data,'A_svdKrylov.csv')));
ieee5_B_svdkrylov = readtable(strcat(path,strcat(ieee5_system_data,'B_svdKrylov.csv')));
ieee5_C_svdkrylov = readtable(strcat(path,strcat(ieee5_system_data,'C_svdKrylov.csv')));
ieee5_D_svdkrylov = readtable(strcat(path,strcat(ieee5_system_data,'D_svdKrylov.csv')));
ieee5_states_svdkrylov = readtable(strcat(path,strcat(ieee5_system_data,'states_svdKrylov.csv')));
ieee5_initial_states_svdkrylov = readtable(strcat(path,strcat(ieee5_system_data,'initial_states_svdKrylov.csv')));
ieee5_output_svdkrylov = readtable(strcat(path,strcat(ieee5_system_data,'output_svdKrylov.csv')));

ieee5_A_approx_bisimulation = readtable(strcat(path,strcat(ieee5_system_data,'A_approximateBisimulation.csv')));
ieee5_B_approx_bisimulation = readtable(strcat(path,strcat(ieee5_system_data,'B_approximateBisimulation.csv')));
ieee5_C_approx_bisimulation = readtable(strcat(path,strcat(ieee5_system_data,'C_approximateBisimulation.csv')));
ieee5_D_approx_bisimulation = readtable(strcat(path,strcat(ieee5_system_data,'D_approximateBisimulation.csv')));
ieee5_initial_states_approx_bisimulation = readtable(strcat(path,strcat(ieee5_system_data,'initial_states_approximateBisimulation.csv')));
ieee5_states_approx_bisimulation = readtable(strcat(path,strcat(ieee5_system_data,'states_approximateBisimulation.csv')));
ieee5_output_approx_bisimulation = readtable(strcat(path,strcat(ieee5_system_data,'output_approximateBisimulation.csv')));

ieee5_A_spectral_projection = table2array(ieee5_A_spectral_projection);
ieee5_B_spectral_projection = table2array(ieee5_B_spectral_projection);
ieee5_C_spectral_projection = table2array(ieee5_C_spectral_projection);
ieee5_D_spectral_projection = table2array(ieee5_D_spectral_projection);
ieee5_states_spectral_projection = table2array(ieee5_states_spectral_projection);
ieee5_initial_states_spectral_projection = table2array(ieee5_initial_states_spectral_projection);
ieee5_output_spectral_projection = table2array(ieee5_output_spectral_projection);

ieee5_A_svdkrylov = table2array(ieee5_A_svdkrylov);
ieee5_B_svdkrylov = table2array(ieee5_B_svdkrylov);
ieee5_C_svdkrylov = table2array(ieee5_C_svdkrylov);
ieee5_D_svdkrylov = table2array(ieee5_D_svdkrylov);
ieee5_states_svdkrylov = table2array(ieee5_states_svdkrylov);
ieee5_initial_states_svdkrylov = table2array(ieee5_initial_states_svdkrylov);
ieee5_output_svdkrylov = table2array(ieee5_output_svdkrylov);

ieee5_A_approx_bisimulation = table2array(ieee5_A_approx_bisimulation);
ieee5_B_approx_bisimulation = table2array(ieee5_B_approx_bisimulation);
ieee5_C_approx_bisimulation = table2array(ieee5_C_approx_bisimulation);
ieee5_D_approx_bisimulation = table2array(ieee5_D_approx_bisimulation);
ieee5_states_approx_bisimulation = table2array(ieee5_states_approx_bisimulation);
ieee5_initial_states_approx_bisimulation = table2array(ieee5_initial_states_approx_bisimulation);
ieee5_output_approx_bisimulation = table2array(ieee5_output_approx_bisimulation);

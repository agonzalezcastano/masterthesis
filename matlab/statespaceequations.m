path = '/Users/amparogonzalezcastano/Documents/GitHub/masterthesis/results/';

A_var_spectral_projection = readtable(strcat(path,'iee34_reduced_A_spectralProjection.csv'));
B_var_spectral_projection = readtable(strcat(path,'iee34_reduced_B_spectralProjection.csv'));
C_var_spectral_projection = readtable(strcat(path,'iee34_reduced_C_spectralProjection.csv'));
D_var_spectral_projection = readtable(strcat(path,'iee34_reduced_D_spectralProjection.csv'));

A_var_svdkrylov = readtable(strcat(path,'iee34_reduced_A_svdKrylov.csv'));
B_var_svdkrylov = readtable(strcat(path,'iee34_reduced_B_svdKrylov.csv'));
C_var_svdkrylov = readtable(strcat(path,'iee34_reduced_C_svdKrylov.csv'));
D_var_svdkrylov = readtable(strcat(path,'iee34_reduced_D_svdKrylov.csv'));

A_var_approx_bisimulation = readtable(strcat(path,'iee34_reduced_A_approximateBisimulation.csv'));
B_var_approx_bisimulation = readtable(strcat(path,'iee34_reduced_B_approximateBisimulation.csv'));
C_var_approx_bisimulation = readtable(strcat(path,'iee34_reduced_C_approximateBisimulation.csv'));
D_var_approx_bisimulation = readtable(strcat(path,'iee34_reduced_D_approximateBisimulation.csv'));
inputs_approx_bisimulation = readtable(strcat(path,'iee34_reduced_inputs_approximateBisimulation.csv'));
states_approx_bisimulation = readtable(strcat(path,'iee34_reduced_initial_states_approximateBisimulation.csv'));

initial_states = test.x0;
states = test.xss;
output = test.yss;
input = test.uss;

path = '/Users/amparogonzalezcastano/Documents/GitHub/masterthesis/systemExample/data/';

writematrix(initial_states,'ieee34_part_data_initial_states.csv');
writematrix(states, 'ieee34_part_data_states.csv');
writematrix(output, 'ieee34_part_data_output.csv');
writematrix(input, 'ieee34_part_data_inputs.csv');
%path = '/Users/amparogonzalezcastano/Documents/GitHub/masterthesis/results/';
%initial_outputs = readtable(strcat(path,'ieee34_part_data_output.csv'));
%initial_inputs = readtable(strcat(path,'ieee34_part_data_inputs.csv'));
%initial_states = readtable(strcat(path,'ieee34_reduced_part_initial_states_spectralProjection.csv'));

%A_part = table2array(A_part);
%B_part = table2array(B_part);
%C_part = table2array(C_part);
%D_part = table2array(D_part);

A_var_approx_bisimulation = table2array(A_var_approx_bisimulation);
B_var_approx_bisimulation = table2array(B_var_approx_bisimulation);
C_var_approx_bisimulation = table2array(C_var_approx_bisimulation);
D_var_approx_bisimulation = table2array(D_var_approx_bisimulation);

states_approx_bisimulation = table2array(states_approx_bisimulation);
%initial_inputs = table2array(initial_inputs);
%initial_states = table2array(initial_states);
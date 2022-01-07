initial_states = test.x0;
states = test.xss;
output = test.yss;
input = test.uss;

path = '/Users/amparogonzalezcastano/Documents/GitHub/masterthesis/systemExamples/data/';

writematrix(initial_states, strcat(path,'ieee34_part_data_initial_states.csv'));
writematrix(states, strcat(path,'ieee34_part_data_states.csv'));
writematrix(output, strcat(path,'ieee34_part_data_output.csv'));
writematrix(input, strcat(path,'ieee34_part_data_inputs.csv'));
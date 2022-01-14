%First, the file struct_ieee34 and struct_ieee34_part must be uploaded to
%matlab
% Both of these file contain a variable called test, from where the
% information is extracted

A = test.A;
B = test.B;
C = test.C;
D = test.D;
initial_states = test.x0;
states = test.xss;
output = test.yss;
input = test.uss;

initial_states_str = num2str(initial_states);
states_str = num2str(states);
inputs_str = num2str(input);
output_str = num2str(output);

path = '/Users/amparogonzalezcastano/Documents/GitHub/masterthesis/systemExamples/data/';

writematrix(A, strcat(path,'ieee34_part_data_A.csv'));
writematrix(B, strcat(path,'ieee34_part_data_B.csv'));
writematrix(C, strcat(path,'ieee34_part_data_C.csv'));
writematrix(D, strcat(path,'ieee34_part_data_D.csv'));
writematrix(initial_states_str, strcat(path,'ieee34_part_data_initial_states.csv'));
writematrix(states_str, strcat(path,'ieee34_part_data_states.csv'));
writematrix(output_str, strcat(path,'ieee34_part_data_output.csv'));
writematrix(inputs_str, strcat(path,'ieee34_part_data_inputs.csv'));
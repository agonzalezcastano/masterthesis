%A = [0 1; -1 -1];
%B = [0; 1];
%C = [1 0];
%D = 0;

%input = [ 5; 5];

%states_calc = -(A\B) * input;
states_calc = linsolve(-A, B*input);

output_calc = C*states_calc;
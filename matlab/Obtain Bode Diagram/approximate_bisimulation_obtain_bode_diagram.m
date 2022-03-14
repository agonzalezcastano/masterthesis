original_sys = ss(A,B,C,D);

ieee34_sys_approx_bisimulation = ss(ieee34_A_approx_bisimulation, ieee34_B_approx_bisimulation, ieee34_C_approx_bisimulation, ieee34_D_approx_bisimulation);
ieee18_sys_approx_bisimulation = ss(ieee18_A_approx_bisimulation, ieee18_B_approx_bisimulation, ieee18_C_approx_bisimulation, ieee18_D_approx_bisimulation);
ieee7_sys_approx_bisimulation = ss(ieee7_A_approx_bisimulation, ieee7_B_approx_bisimulation, ieee7_C_approx_bisimulation, ieee7_D_approx_bisimulation);
ieee5_sys_approx_bisimulation = ss(ieee5_A_approx_bisimulation, ieee5_B_approx_bisimulation, ieee5_C_approx_bisimulation, ieee5_D_approx_bisimulation);

bode(original_sys, ieee34_sys_approx_bisimulation, ieee18_sys_approx_bisimulation, ieee7_sys_approx_bisimulation, ieee5_sys_approx_bisimulation)
grid on
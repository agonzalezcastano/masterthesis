original_sys = ss(A,B,C,D);

ieee34_sys_svdKrylov = ss(ieee34_A_svdKrylov, ieee34_B_svdKrylov, ieee34_C_svdKrylov, ieee34_D_svdKrylov);
ieee18_sys_svdKrylov = ss(ieee18_A_svdKrylov, ieee18_B_svdKrylov, ieee18_C_svdKrylov, ieee18_D_svdKrylov);
ieee7_sys_svdKrylov = ss(ieee7_A_svdKrylov, ieee7_B_svdKrylov, ieee7_C_svdKrylov, ieee7_D_svdKrylov);
ieee5_sys_svdKrylov = ss(ieee5_A_svdKrylov, ieee5_B_svdKrylov, ieee5_C_svdKrylov, ieee5_D_svdKrylov);

bode(original_sys, ieee34_sys_svdKrylov, ieee18_sys_svdKrylov, ieee7_sys_svdKrylov, ieee5_sys_svdKrylov)
grid on
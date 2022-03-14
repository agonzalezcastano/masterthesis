opt = bodeoptions;
opt.FreqScale = 'Linear';

original_sys = ss(A,B,C,D);

% ieee34_sys_spectral_projection = ss(ieee34_A_spectral_projection, ieee34_B_spectral_projection, ieee34_C_spectral_projection, ieee34_D_spectral_projection);
% ieee18_sys_spectral_projection = ss(ieee18_A_spectral_projection, ieee18_B_spectral_projection, ieee18_C_spectral_projection, ieee18_D_spectral_projection);
% ieee7_sys_spectral_projection = ss(ieee7_A_spectral_projection, ieee7_B_spectral_projection, ieee7_C_spectral_projection, ieee7_D_spectral_projection);
ieee5_sys_spectral_projection = ss(ieee5_A_spectral_projection, ieee5_B_spectral_projection, ieee5_C_spectral_projection, ieee5_D_spectral_projection);

rng("default")
h = bodeplot(original_sys, opt);
setoptions(h,'FreqUnits','Hz','PhaseVisible','off');

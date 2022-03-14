Amparo Gonzalez Castaño - Master Thesis - Comparison of Model Order Reduction Methods for Power Grids
#####
Folders:
- systemExamples: Contains the files that transform the state-spaces matrices inside the 'data' folder to python's matrices.
    - Data: Contains all the state-space matrices obtained from MATLAB of the following systems: IEEE34, IEEE18, IEEE7 and IEE5.

- svdKrylovMethod: Contains all the files regarding the SVD-Krylov method.
- spectralProjectionModalTruncationMethod: Contains all the files regarding the Spectral Projection Modal Truncation method.
- approximateBisimulationMethod: Contains all the files regarding the Approximate Bisimulation method.

- results: Contains a file for calculating the error (calculateError.py), a file that transforms python matrices to MATLAB (transformDataToMatlab.py) and the reduced systems state-space matrices.

- matlab: Contains the MATLAB files for obtaining the original system state-space matrices, the files to obtain the Bode diagram, the files to obtain the Eigenvalues, the files to obtain the reduced system state-space matrices, the simulations and the IEEE34 matrices.

#####
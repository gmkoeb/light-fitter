# light-fitter
Fits JxV curves obtained from solar cells under illumination and calculates important parameters

## How does this works?
The program reads a .dat or .txt file with experimental data from JxV (current density vs applied voltage) measurements made in solar cells under illumination. After that, it picks the best theoretical function from a list with polynomials and exponential functions to perform the fit. When it finds the better function, the program prints all useful parameters for solar cell characterization (Rs, Rsh, Voc, Jsc and PCE), and plots the theoretical function used alongside with the experimental data.

## Examples


# light-fitter
Fits JxV curves obtained from solar cells under illumination and calculates important parameters

## How does this works?
The program reads a .dat or .txt file with experimental data from JxV (current density vs applied voltage) measurements made in solar cells under illumination. After that, it picks the best theoretical function from a list with polynomials and exponential functions to perform the fit. When it finds the better function, the program prints all useful parameters for solar cell characterization (Rs, Rsh, Voc, Jsc and PCE), and plots the theoretical function used alongside with the experimental data.

## Examples

```
~$ python3 light.py
 Rs= 6.802274180232417 Ohm m²
 Rsh= 51.78864221518462 Ohm m²
 Voc= 23.01824827450167 V
 Jsc= -1.42867 A/m²
 FF= 38.999896184246644 %
 PCE= 3.7142494517810594 %
```
![Sample](./images/luzexemplo.png)

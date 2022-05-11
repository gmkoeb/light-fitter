import numpy as np
from numpy import arange
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.optimize import root
from sklearn.metrics import r2_score
import func as fc

data = np.loadtxt('testdata.txt')

x = data[:, 0]
y = data[:, 1]

n = len(data)

picker = data[:,:]
max_x_y = 0
maximum_value = 0
for line in picker:
    value = abs(line[0]) * abs(line[1])
    if value > maximum_value:
        maximum_value= value
        max_x_y = line
Vmax=max_x_y[0]
Jmax=max_x_y[1]

def call_function(function, degree):
    popt1, _ = curve_fit(function, x, y)
    a, b, c, d, e, f, g, h, i, j, k  = popt1
    coeffs = [a, b, c, d, e, f, g, h, i, j, k]
    
    res=root(function,0.1, args=(a,b,c,d,e,f,g,h,i,j,k)).x[0]
    x_line = arange(min(x), max(x), 0.001)
    y_line = function(x_line, a, b, c, d, e, f, g, h, i, j, k)
    xt = np.linspace(0, res, n)
    f = coeffs[degree]
    for index in range (1, degree + 1):
        f += coeffs[index-1] * xt**index
    
    correlation_matrix = np.corrcoef(y, f)
    correlation_xy = correlation_matrix[0,1]
    r2 = correlation_xy**2
    return r2

def function_e0(x, a, b):
    return a + np.exp(b*x)
def e0():
    popt1, _ = curve_fit(function_e0, x, y)
    a, b = popt1
    res=root(function_e0, 0.1, args=(a,b)).x[0]
    x_line = arange(min(x), max(x), 0.001)
    y_line = function_e0(x_line, a, b)
    xt = np.linspace(0, res, n)
    f = a + np.exp(b*xt)
    correlation_matrix = np.corrcoef(y, f)
    correlation_xy = correlation_matrix[0,1]
    r2 = correlation_xy**2
    return r2

def function_e1(x,a,b,c):
    return a*x + np.exp(b*x) + c
def e1():
    popt1, _ = curve_fit(function_e1, x, y)
    a, b, c = popt1
    res=root(function_e1, 0.1, args=(a,b,c)).x[0]
    x_line = arange(min(x), max(x), 0.001)
    y_line = function_e1(x_line, a, b, c)
    xt = np.linspace(0, res, n)
    f = a*xt + np.exp(b*xt) + c
    correlation_matrix = np.corrcoef(y, f)
    correlation_xy = correlation_matrix[0,1]
    r2 = correlation_xy**2
    return r2

def function_e2(x, a, b, c, d):
    return a*x + np.exp(b*x) + c * x**2 + d
def e2():
    popt1, _ = curve_fit(function_e2, x, y)
    a, b, c, d=popt1
    res=root(function_e2, 0.1, args=(a,b,c,d)).x[0]
    x_line = arange(min(x), max(x), 0.001)
    y_line = function_e2(x_line, a, b, c, d)
    xt = np.linspace(0, res, n)
    f = a*xt + np.exp(b*xt) + c * xt**2 + d
    correlation_matrix = np.corrcoef(y, f)
    correlation_xy = correlation_matrix[0,1]
    r2 = correlation_xy**2
    return r2

results = []

results.append([call_function(fc.sq,2), fc.sq, 2])
results.append([call_function(fc.tr,3), fc.tr, 3])
results.append([call_function(fc.fo,4), fc.fo, 4])
results.append([call_function(fc.fi,5), fc.fi, 5])
results.append([call_function(fc.si,6), fc.si, 6])
results.append([call_function(fc.se,7), fc.se, 7])
results.append([call_function(fc.ei,8), fc.ei, 8])
results.append([call_function(fc.ni,9), fc.ni, 9])
results.append([call_function(fc.te,10),fc.te, 10])

results.append([e0(), function_e0, 0])

results.append([e1(), function_e1, 0])

results.append([e2(), function_e2, 0])

ma=results[0]
for i in results:
    if i[0]>ma[0]:
        ma=i

chosen_function = ma[1]
degree = ma[2]
xt=0
f=0
if chosen_function == function_e0:
    popt1, _ = curve_fit(function_e0, x, y)
    a, b = popt1
    res=root(function_e0, 0.1, args=(a,b)).x[0]
    x_line = arange(min(x), max(x), 0.001)
    y_line = function_e0(x_line, a, b)
    xt = np.linspace(0, res, n)
    f = a + np.exp(b*xt)
    print (res)

elif chosen_function == function_e1:
    popt1, _ = curve_fit(function_e1, x, y)
    a, b, c = popt1
    res=root(function_e1, 0.1, args=(a,b,c)).x[0]
    x_line = arange(min(x), max(x), 0.001)
    y_line = function_e1(x_line, a, b, c)
    xt = np.linspace(0, res, n)
    f = a*xt + np.exp(b*xt) + c
    print (res)
elif chosen_function == function_e2:
    popt1, _ = curve_fit(function_e2, x, y)
    a, b, c, d=popt1
    res=root(function_e2, 0.1, args=(a,b,c,d)).x[0]
    x_line = arange(min(x), max(x), 0.001)
    y_line = function_e2(x_line, a, b, c, d)
    xt = np.linspace(0, res, n)
    f = a*xt + np.exp(b*xt) + c * xt**2 + d 
    print (res)
else:
    popt1, _ = curve_fit(chosen_function, x, y)
    a, b, c, d, e, f, g, h, i, j, k  = popt1
    coeffs = [a, b, c, d, e, f, g, h, i, j, k]
    
    res=root(chosen_function,0.1, args=(a,b,c,d,e,f,g,h,i,j,k)).x[0]
    x_line = arange(min(x), max(x), 0.001)
    y_line = chosen_function(x_line, a, b, c, d, e, f, g, h, i, j, k)
    xt = np.linspace(0, res, n)
    f = coeffs[degree]
    for index in range (1, degree + 1):
        f += coeffs[index-1] * xt**index

df=np.gradient(f)/np.gradient(xt)
Rs=1/df[n-1]
Rsh=1/df[0]
Voc=res
Jsc=y[0]
FF=((Vmax*Jmax)/(Voc*Jsc))*100
EF=abs((Voc*Jsc*FF)/(345.3))  #user needs to provide the incoming power from the light source (in this case 345.3)
        
print (" Rs=",Rs,"Ohm m²")

print (" Rsh=",Rsh,"Ohm m²")

print (" Voc=",Voc,"V")

print(" Jsc=",Jsc,"A/m²")

print(" FF=",FF,"%")
print(" PCE=",EF,"%")

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title('JXV')    

ax1.set_xlabel('V(V)')

ax1.set_ylabel('J(A/m²)')
plt.plot(x, y,'ko', label='Experimental', markevery=37)
plt.plot(xt, f,'r-', label='Fit, R²={}'.format(ma[0]))




leg = ax1.legend()
plt.show()


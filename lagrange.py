import numpy as np
from scipy.optimize import fsolve
import warnings
#warnings.filterwarnings('ignore', 'The iteration is not making good progress')

Sa = 200
Sm = 100
n = 5000
mu1 = 500
mu2 = 150
sigma1 = 25
sigma2 = 10
f = 0.9

def func(X):
    x = X[0]
    y = X[1]
    L = X[2] # this is the multiplier. lambda is a reserved keyword in python
    return (4*x+4*y  - L * (x**2 + y**2 -n))

def dfunc(X):
    dLambda = np.zeros(len(X))
    h = 1e9 # this is the step size used in the finite difference.
    for i in range(len(X)):
        dX = np.zeros(len(X))
        dX[i] = h
        dLambda[i] = (func(X+dX)-func(X-dX))/(2*h);
    return dLambda

# this is the max
X1 = fsolve(dfunc, [1, 1, 0])
print (X1, func(X1))

# this is the min
X2 = fsolve(dfunc, [-1, -1, 0])
print (X2, func(X2))
print(abs(X2[0]))

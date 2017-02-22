'''import warnings
warnings.filterwarnings('ignore', 'The iteration is not making good progress')
return (u1**2+u2**2  -
L*(Sa/(1-Sm/(sigma1*u1 + mu1))/((f*(sigma1*u1 + mu1))**2)/(sigma2*u2 + mu2))**
1/-1/3*(f*(sigma1*u1 + mu1))/(sigma2*u2 + mu2) -n)'''
import math
import numpy as np
from decimal import Decimal
from scipy.optimize import fsolve
import sympy as sp

Sa = 220
Sm = 0

n = np.arange(10000,260000,10000)

mu1 = 310
sigma1 = 10

mu2 = 85
sigma2 = 10

f = 0.85

def func(X,n):
    u1 = X[0]
    u2 = X[1]
    L = X[2] # this is the multiplier. lambda is a reserved keyword in python

    'function --> f(u1,u2) = u1**2 + u2**2'
    'constraint --> g(u1,u2) = (Snf/a)**1/b = n'

    Snf = Sa/(1-Sm/(sigma1*u1 + mu1))
    a = ((f*(sigma1*u1 + mu1))**2)/(sigma2*u2 + mu2)
    b = (-1/4.35)* math.log10(f*(sigma1*u1 + mu1)/(sigma2*u2 + mu2))

    return (u1**2+u2**2  - L * ((1*(Snf/a)**(1/b)) - n))

def dfunc(X,n):
    dLambda = np.zeros(len(X))
    h = 1e-3 # this is the step size used in the finite difference.
    r=0
    for i in range(len(X)):
        dX = np.zeros(len(X))
        dX[i] = h
        dLambda[i] = (func(X+dX,n)-func(X-dX,n))/(2*h);
    return dLambda


'''for iter_n in n:
    print("for n = {0} dfunc = {1}".format(iter_n,fsolve(dfunc,([1,1,0]),iter_n)))
'''

for a in n:
    x1 = fsolve(dfunc,([1,1,0]),a)
    print(x1[0])


for nn in range(10000,260000,10000):

    v1, v2 = sp.symbols('v1 v2', real=True)

    Snf = Sa/(1-Sm/(sigma1*v1 + mu1))
    a = ((f*(sigma1*v1 + mu1))**2)/(sigma2*v2 + mu2)
    b = (-1/4.35)* sp.log(f*(sigma1*v1 + mu1)/(sigma2*v2 + mu2),10)
    Nf = (Snf/a)**(1/b)
    g = 1-(nn/Nf)

    fu1 = sp.diff(g,v1).subs({v1:x1[0], v2:x1[1]})
    fu2 = sp.diff(g,v2).subs({v1:x1[0], v2:x1[1]})


    print(sp.simplify(fu1))


########


    #

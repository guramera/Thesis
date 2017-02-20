import sympy as sp
import mpmath
import numpy as np
import math

Sa = 220
Sm = 0

mu1 = 310
sigma1 = 15

mu2 = 95
sigma2 = 5

f = 0.9
n = 150000

u1, u2 = sp.symbols('u1 u2', real=True)

Snf = Sa/(1-Sm/(sigma1*u1 + mu1))
a = ((f*(sigma1*u1 + mu1))**2)/(sigma2*u2 + mu2)
b = (-1/4.35)* sp.log(f*(sigma1*u1 + mu1)/(sigma2*u2 + mu2),10)
Nf = (Snf/a)**(1/b)
g = 1-(n/Nf)

fu1 = sp.diff(g,u1).subs({u1:0.321013690069, u2:0.082765635388})
fu2 = sp.diff(g,u2).subs({u1:0.321013690069, u2:0.082765635388})

print(sp.simplify(fu1), sp.simplify(fu2))




'''fu1 = sympy.diff((Sa/(1-Sm/(sigma1*u1 + mu1))/((f*(sigma1*u1 + mu1))**2)/(sigma2*u2 + mu2))**(1/b), u1).subs({u1:7.67759992, u2:17.3511262})
print(sympy.simplify(fu1))

fu2 = sympy.diff((Sa/(1-Sm/(sigma1*u1 + mu1))/((f*(sigma1*u1 + mu1))**2)/(sigma2*u2 + mu2))**(1/b), u2).subs({u1:7.67759992, u2:17.3511262})
print(sympy.simplify(fu2))'''

from sympy import *
#import math

x = Symbol('x')
y = (sin(5*x))**2 + exp(5*x)

y_diff5 = y.diff(x, 5)
print(y_diff5)
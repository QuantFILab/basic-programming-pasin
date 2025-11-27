import numpy as np
from sympy import *
from math import factorial
from matplotlib import pyplot as plt

# function for finding term Ti of Taylor Series 
def Taylor_i(y, n, a):
    y_dif = y.diff(x, n)
    y_dif = lambdify(x, y_dif)
    Ti = y_dif(a)/factorial(n) * (x-a)**n
    return Ti

def Sum_Taylor(y, n, a):
    Tn = 0
    for i in range(n+1):
        Tn_i = Taylor_i(y, i, a)
        Tn = Tn + Tn_i
    return Tn

#main function
x = Symbol('x')
y = cos(x)
n = 20
a = 0
Tnn = Sum_Taylor(y, n, a)
Tnnx = lambdify(x, Tnn)

x = np.linspace(-10, 10, 1000)
plt.plot(x, Tnnx(x))
plt.show()

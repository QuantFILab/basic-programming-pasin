import numpy as np #1
from sympy import * #1
from math import factorial
from matplotlib import pyplot as plt #1

def TS_i(y, i, a):  #ห้ามแก้
    y_dif = y.diff(x, a) 
    y_dif = lambdify(x, y_dif) #1
    Ti = y_dif(a)/factorial(i) * (x-a)**i #0
    return Ti #1

def Sum_TS_i(y, n, a): #ห้ามแก้
    Tn = 0
    for i in range(n+1): #1
        Tn_i = TS_i(y, i, a) #1
        Tn = Tn + Tn_i
    return Tn

#main function
x = Symbol('x')
func_y = exp(x)
n = 100
a = 0
Tnn = Sum_TS_i(func_y, n, a) #1
Tnn = lambdify(x, Tnn)

x = np.linspace(-20, 20, 1000)
plt.plot(x, Tnn(x))
plt.show() #1

#9*5 = 45
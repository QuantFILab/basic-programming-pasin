# 1-Dimensional Heat Transfer
# u_t = alpha * u_xx
# B.C. : u(0,t) = a , u(L,t) = b ; t>0
# I.C. : u(x,0) = f(x) ; 0<x<L

import numpy as np
import matplotlib.pyplot as plt

alpha = 1.8
L = 3 * np.pi # length of domain 2*Pi
n = 20 # seperate the domain into 10 pieces equally
t_final = 2

dx = L/n
dt = 0.5 * dx**2 / alpha
N = int(t_final/dt)

# Dirichlet Boundary Condition:

# B.C. : u(0,t) = 0 , u(L,t) = 0 ; t>0
u_0t = 15
u_nt = 15

# I.C. : u(x,0) = 100 ; 0<x<L
#u_x0 = 100 
#u = np.ones(n+1) * u_x0

# I.C. : u(x,0) = 100 * sin(x) ; 0<x<L
x = np.linspace(0, L, n+1)
u = 150 * np.cos(x) 

u[0] = u_0t
u[-1] = u_nt

x = np.linspace(0, L, n+1)

for j in range(1,N+1):
    w = u.copy()
    for i in range(1,n):
        u[i] = w[i] + alpha * dt *((w[i+1] - 2*w[i] + w[i-1])/dx**2)
    #print(f"Round {j} : {u}")
    plt.clf()
    plt.xlim(0,L)
    plt.ylim(-150,150)
    plt.plot(x,u)
    #plt.title(f"Distribution at round {j}")
    #plt.title(f"Distribution at time {j*dt}")
    plt.title("Distribution at time {:.4f} [s]".format(j*dt))
    #plt.title("Average Temperature {:.4f}".format(np.average(u)))
    plt.pause(0.1)

plt.show()
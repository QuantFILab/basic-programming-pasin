# 1-Dimensional Heat Transfer
# u_t = alpha * u_xx
# B.C. : u(0,t) = a , u(L,t) = b ; t>0
# I.C. : u(x,0) = f(x) ; 0<x<L

import numpy as np
import matplotlib.pyplot as plt

alpha = 0.1

L = 2 * np.pi # length of domain 2*Pi
n = 100
dx = L/n 
dt = 0.5 * dx**2 / alpha
t_final = 1

# Dirichlet Boundary Condition:

# B.C. : u(0,t) = 0 , u(L,t) = 0 ; t>0
u_0t = 0
u_nt = 0

# I.C. : u(x,0) = 100 ; 0<x<L
#u_x0 = 100 
#u = np.ones(n+1) * u_x0

# I.C. : u(x,0) = 100 * sin(x) ; 0<x<L
x = np.linspace(0, L, n+1)
u = 100 * np.sin(x) 

u[0] = u_0t
u[-1] = u_nt

# Visualizing with a plot
fig, axis = plt.subplots()
pcm = axis.pcolormesh([u], cmap=plt.cm.jet, vmin=-100, vmax=100)
plt.colorbar(pcm, ax=axis)
axis.set_ylim(-10,11)

# Simulating
counter = 0
while counter < t_final:
    w = u.copy()
    for i in range(1,n):
        u[i] = w[i] + alpha * dt *((w[i+1] - 2*w[i] + w[i-1])/dx**2)
    counter += dt
    #print(f'time = {counter} and average temperature = {np.average(u)}')
    pcm.set_array([u])
    axis.set_title("Distribution at time {:.3f} [s]".format(counter))
    plt.pause(0.1)

plt.show()
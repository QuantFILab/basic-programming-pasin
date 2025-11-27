import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

print("Start : . . .")
print("----------------------------")
print("Solution of 2D Heat Equation")
print("----------------------------")

w, h = input("Define your domain's width and height : ").split()
print(f"Width = {w} and Height = {h}")

plate_width = int(w)
plate_height = int(h)

it = input("Define number of iterations : ")
max_iter_time = int(it)

nx = 51
ny = 51

alpha = 4
delta_x = plate_width/(nx-1)
delta_y = plate_height/(ny-1)

delta_t = (delta_x ** 2)/(4 * alpha)
gamma_x = (alpha * delta_t)/(delta_x ** 2)
gamma_y = (alpha * delta_t)/(delta_y ** 2)

# initialize the solution: the grid of u(k,i,j)
u = np.empty((max_iter_time,ny,nx))

# initial condition everywhere inside the grid
u_initial = 0
#u_initial = np.random.uniform(low=28.5, high=55.5, size=(ny,nx))

# boundary contitions:
u_top = 0.0
u_bottom = 0.0
u_left = 0.0
u_right = 0.0


# set the initial condition
u[0, :, :] = u_initial

# set boundary conditions
#u[:, -1:,   :] = u_top
#u[:,   :1,  :] = u_bottom
#u[:,   :,   :1] = u_left
#u[:,   :, -1:] = u_right


# define a function to calculate the solution
# of each time k

def calculate(u):
    for k in range(0, max_iter_time - 1, 1):
        for i in range(1, ny - 1, 1):
            for j in range(1, nx - 1, 1):
                u[k + 1, i, j] = u[k][i][j] + gamma_x * (u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j])
        u[k:, -1,  :] = u[k:, -2,  :] #du/dy = 0 at u_top
        u[k:,  1,  :] = u[k:,  2,  :] #du/dy = 0 at u_bottom
        u[k:,   :, 1] = u[k:,   :, 2] #du/dx = 0 at u_left
        u[k:,  :, -1] = u[k:,  :, -2] #du/dx = 0 at u_right
        u[k:, 25, 25] = 100*k
    return u    

def plot_heat_map(u_k, k):
    # clear the current figure
    plt.clf()
    
    plt.title(f'Temperature at t = {k * delta_t:.3f} unit time')
    plt.xlabel("x")
    plt.ylabel("y")
    
    # plot u_k (u at time-step k)
    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)
    plt.colorbar
    
    return plt


# do the calculation here
u = calculate(u)

def animate(k):
    plot_heat_map(u[k], k)

anim = FuncAnimation(plt.figure(), animate, interval=5, frames=max_iter_time, repeat=False)
anim.save("2d_heat3.gif")

animate(max_iter_time - 1)

plt.show()

print("Done !!")




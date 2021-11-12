import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import matplotlib
from solve import dumptimeintegrate

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

## initialise parameters: domain, coefficients etc
lx = 10
ly = 10  ## domain length
nx = 201
ny = 201
u0 = 2
v0 = 0
g = 9.8
H = 1

X = np.linspace(0, lx, nx)
dx = X[1] - X[0]
Y = np.linspace(0, ly, ny)
dy = Y[1] - Y[0]
x, y = np.meshgrid(X, Y)
u = 0 * x + 0 * y
v = 0 * x + 0 * y
harg = -((x - 5) ** 2 + (y - 5) ** 2) / 0.3
h = 10 * np.exp(harg)

cfl = 0.5  # CFL number
stepS = np.sqrt(dx ** 2 + dy ** 2)
dt = cfl * stepS / (u0 + math.sqrt(g * H))
tend = 20
nt = int(round(tend / dt))  # number of time steps
n = 0  # counter
t = 0
# method = "Euler"
# method = "RK2"
method = "RK4"
order = 6

out, times = dumptimeintegrate(x, y, nx, ny, dx, dy, order, u0, v0, H, g, 5, dt, method)
zarray = np.array(out)

print(zarray.shape)

def update_plot(frame_number, zarray, plot):
    plot[0].remove()
    plot[0] = ax.plot_surface(x, y, zarray[frame_number, 0, :, :], cmap="magma")


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("h")
plot = [ax.plot_surface(x, y, zarray[0, 0, :, :], color="0.75", rstride=1, cstride=1)]
ax.set_zlim(-2, 10)
ani = animation.FuncAnimation(
    fig, update_plot, len(out), fargs=(zarray, plot), interval=10
)
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:31:39 2016
Variation of the Lorenz variable z as a function of time,
using Euler method.
@author: nightwing
"""

from tqdm import tqdm
import matplotlib.pyplot as plt


def LORENZ_MODEL(x, y, z, r):
    delta = 10           # argument delta
    b = 8.0 / 3          # argument b
    t = 0                # initial time
    dt = 0.0001          # time step
    t_end = 50           # end of time
    time = []            # this list store the time
    displacement_z = []  # this list store the z
    while t <= t_end:
        time.append(t)
        displacement_z.append(z)
        x += (delta * (y - x)) * dt
        y += (- x * z + r * x - y) * dt
        z += (x * y - b * z) * dt
        t += dt
    return [time, displacement_z]

# -----------------caculate------------------
situations = []  # this list store different trajectories

for r in tqdm([5, 10, 25]):
    situations.append(LORENZ_MODEL(1.0, 0.0, 0.0, r))

# -----------------graph---------------
plt.title("Lorenz model  z versus time")
plt.xlabel("time")
plt.ylabel("z")
for i in range(len(situations)):
    plt.plot(situations[i][0], situations[i][1], "k-")
plt.text(10, 2, "r = 5")
plt.text(10, 6, "r = 10")
plt.text(30, 40, "r = 25")
plt.show()
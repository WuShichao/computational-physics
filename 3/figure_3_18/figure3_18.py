# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:20:08 2016
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
    t_end = 100          # end of time
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

for r in tqdm([160, 165.4]):
    situations.append(LORENZ_MODEL(1.0, 0.0, 0.0, r))

# -----------------graph---------------
plt.subplot(211)
plt.title("Lorenz model  z versus time")
plt.text(40, 300, "r = 160.0")
plt.ylabel("z")
plt.plot(situations[0][0], situations[0][1], "k-")
plt.subplot(212)
plt.text(40, 300, "r = 165.4")
plt.xlabel("time")
plt.ylabel("z")
plt.plot(situations[1][0], situations[1][1], "k-")
plt.show()

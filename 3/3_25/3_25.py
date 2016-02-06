# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 16:04:27 2016
Variation of the Lorenz variable z as a function of time, with different r
using Euler method.
@author: nightwing
"""

from tqdm import tqdm
from numpy import linspace
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
AMOUNTS = 500
index = 0

for r in tqdm(linspace(0, 160, AMOUNTS)):
    situations = LORENZ_MODEL(1.0, 0.0, 0.0, r)
    text = "r = %.4f" % r
    index += 1

    # ---------------graph and save---------------
    plt.figure(figsize=(8, 6))
    plt.title("Lorenz model  z versus time")
    plt.xlabel("time")
    plt.ylabel("z")
    plt.text(40, 300, text)
    plt.plot(situations[0], situations[1], "k-")
    plt.xlim(0, 100)
    plt.ylim(0, 350)
    plt.savefig("%s.png" % index)
    plt.close()

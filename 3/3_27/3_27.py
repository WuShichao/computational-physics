# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:23:34 2016
Phase space plot of the Lorenz model, z versus y, z versus x,
uisng Euler method.
@author: nightwing
"""

import matplotlib.pyplot as plt


def LORENZ_MODEL(x, y, z, r):
    delta = 10           # argument delta
    b = 8.0 / 3          # argument b
    t = 0                # initial time
    dt = 0.0001          # time step
    t_end = 800          # end of time
    displacement_1 = []  # this list store displacement 1
    displacement_2 = []  # this list store displacement 2
    while t <= t_end:
        if t >= 30:  # allow for the decay of initial transients
            if abs(y) < 0.001:
                displacement_1.append(x)
                displacement_2.append(z)
        x += (delta * (y - x)) * dt
        y += (- x * z + r * x - y) * dt
        z += (x * y - b * z) * dt
        t += dt
    return [displacement_1, displacement_2]

# -----------------caculate------------------
init_x = 0
init_y = 1
init_z = 1
phase_space = LORENZ_MODEL(init_x, init_y, init_z, 25)

# --------------graph---------------
plt.figure(figsize=(8, 6))
plt.title("Phase space plot: z versus x when y = 0")
plt.text(-15, 5, "x = %d, y = %d, z = %d" % (init_x, init_y, init_z))
plt.xlabel("x")
plt.ylabel("z")
plt.scatter(phase_space[0], phase_space[1], s=1)
plt.xlim(-20, 20)
plt.ylim(0, 40)
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 21:03:15 2016
Bifurcation diagram of the physical pendulum, using Euler-Cromer method.
@author: nightwing
"""

from tqdm import tqdm
from math import sin,pi
from numpy import linspace
import matplotlib.pyplot as plt

g = 9.8               #gravity acceleration (m/s2)
length = 9.8          #length of the rod (m)
k = g / length        #g/length 
dt = 0.001            #time step (s)
t_end = 3600          #end time (s)
situations = []       #this list store [fd, angle]

#caculate the physical pendulum
def PHYSICAL_PENDULUM(q,fd,freq,theta):
    t = 0                 #initial time (s)
    angular_vel = 0       #initial angular velocity (rad/s) 
    angle = []            #this list store value of angle
    while t <= t_end:
        if t > 2*pi/freq*300: #make sure that the initial transient decayed
            if abs(round(t/(2*pi/freq)) - (t/(2*pi/freq))) < 0.0001: 
                angle.append(theta)
        angular_vel += (-k*sin(theta)-q*angular_vel+fd*sin(freq*t)) * dt
        theta += angular_vel * dt
        if theta > pi:
            theta -= 2*pi
        elif theta < -pi:
            theta += 2*pi
        t += dt
    return [angle]

#-------------caculate (Euler-Cromer method)------------
AMOUNTS = 1000
range_fd = linspace(1.35, 1.5, AMOUNTS)

for F in tqdm(range_fd):
    situations.append(PHYSICAL_PENDULUM(0.5, F, 2/3.0, 0.2))

#----------------graph--------------
plt.title("Bifurcation diagram  $\\theta$ versus Fd")
plt.xlabel("Fd")
plt.ylabel("$\\theta$ (radians)")
for i in range(AMOUNTS):
    FD = [range_fd[i]]
    for THETA in situations[i]:
        plt.scatter(FD*len(THETA),THETA,s=1)
plt.xlim(1.35,1.5)
plt.ylim(1,3)
plt.show()

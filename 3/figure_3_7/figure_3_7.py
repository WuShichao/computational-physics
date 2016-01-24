# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:09:54 2016
delta theta versus time, using Euler-Cromer method
@author: nightwing
"""

from math import sin,pi
import numpy as np
import matplotlib.pyplot as plt

g = 9.8               #gravity acceleration (m/s2)
length = 9.8          #length of the rod (m)
k = g / length        #g/length 
dt = 0.04             #time step (s)
situations = []       #this list store [time, angle]
delta_theta = []      #this list store delta theta 

#caculate the physical pendulum
def PHYSICAL_PENDULUM(q,fd,freq,theta,t_end):
    t = 0                 #initial time (s)
    angular_vel = 0       #initial angular velocity (rad/s) 
    angular_velocity = [] #this list store value of angular velocity
    angle = []            #this list store value of angle
    time = []             #this list store value of time
    while t <= t_end:
        angular_velocity.append(angular_vel)
        angle.append(theta)
        time.append(t)
        angular_vel += (-k*sin(theta)-q*angular_vel+fd*sin(freq*t)) * dt
        theta += angular_vel * dt
        if theta > pi:
            theta -= 2*pi
        elif theta < -pi:
            theta += 2*pi
        t += dt
    return [time,angle]
    
#-------------caculate (Euler-Cromer method)------------
situations.append(PHYSICAL_PENDULUM(0.5, 0.5, 2/3.0, 0.2, 50))
situations.append(PHYSICAL_PENDULUM(0.5, 0.5, 2/3.0, 0.201, 50))
situations.append(PHYSICAL_PENDULUM(0.5, 1.2, 2/3.0, 0.2, 150))
situations.append(PHYSICAL_PENDULUM(0.5, 1.2, 2/3.0, 0.201, 150))
delta_theta.append(abs(np.array(situations[0][1])-np.array(situations[1][1])))
delta_theta.append(abs(np.array(situations[2][1])-np.array(situations[3][1])))

#--------------graph---------------
plt.subplot(121)
plt.title("$\Delta\\theta$ versus time  Fd=0.5")
plt.semilogy(situations[0][0],delta_theta[0],"k-")
plt.xlabel("time (s)")
plt.ylabel("$\Delta\\theta$ (radians)")
plt.subplot(122)
plt.title("$\Delta\\theta$ versus time  Fd=1.2")
plt.semilogy(situations[2][0],delta_theta[1],"k-")
plt.xlabel("time (s)")
plt.ylabel("$\Delta\\theta$ (radians)")
plt.show()
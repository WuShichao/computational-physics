# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:02:10 2016
Compute the total energy of the physical pendulum, 
using Euler-Cromer method.
@author: nightwing
"""

from math import sin,cos,pi
import matplotlib.pyplot as plt

g = 9.8               #gravity acceleration (m/s2)
mass = 1.0            #mass of the pendulum (kg)
length = 9.8          #length of the rod (m)
k = g / length        #g/length 
dt = 0.04             #time step (s)
t_end = 60            #end time (s)
situations = []       #this list store [time, angle]

#caculate the physical pendulum
def PHYSICAL_PENDULUM(q,fd,freq,theta):
    t = 0                 #initial time (s)
    angular_vel = 0       #initial angular velocity (rad/s) 
    total_energy = []     #this list store the total energy
    time = []             #this list store value of time
    while t <= t_end:
        time.append(t)
        energy = 0.5*mass*(length*angular_vel)**2 + mass*g*length*(1-cos(theta))
        total_energy.append(energy)        
        angular_vel += (-k*sin(theta)-q*angular_vel+fd*sin(freq*t)) * dt
        theta += angular_vel * dt
        if theta > pi:
            theta -= 2*pi
        elif theta < -pi:
            theta += 2*pi
        t += dt
    return [time,total_energy]
    
#-------------caculate (Euler-Cromer method)------------
for F in [0, 0.5, 1.2]:
    situations.append(PHYSICAL_PENDULUM(0.5, F, 2/3.0, 0.2))

#---------------graph----------------
plt.subplot(311)
plt.title("total energy versus time (Fd=0, 0.5, 1.2)")
plt.plot(situations[0][0],situations[0][1],"k-")
plt.subplot(312)
plt.ylabel("total energy (J)")
plt.plot(situations[1][0],situations[1][1],"k-")
plt.subplot(313)
plt.plot(situations[2][0],situations[2][1],"k-")
plt.xlabel("time (s)")
plt.show()
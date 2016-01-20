# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 19:32:31 2016
Locate the boundary between the overdamped and underdamped regimes, 
using Euler-Cromer.
@author: nightwing
"""

from math import pi
from numpy import linspace
import matplotlib.pyplot as plt

g = 9.8                         #gravity acceleration (m/s2)
length = 1                      #length of the string (m)
k = g / length                  #g/length 
dt = 0.001                      #time step (s)
t_end = 6                       #end time (s)
damped_pendulum = []            #this list store angle and time 

#caculate damped pendulum
def DAMPED(Q):
    t = 0                       #initial time (s)
    theta = 11.5                #initial angle (degrees)
    theta *= (pi/180)           #initial angle (radians)
    angular_vel = 0             #initial angular velocity (rad/s)
    angle = []                  #this list store value of angle
    time = []                   #this list store value of time

    while t <= t_end:
        angle.append(theta)
        time.append(t)
        angular_vel -= (k*theta + Q*angular_vel) * dt
        theta += angular_vel * dt
        t += dt
    return [time,angle]    

#------------------caculate----------------
for q in linspace(5,10,10):
    damped_pendulum.append(DAMPED(q))

#------------------graph------------------    
plt.title("the boundary between the overdamped and underdamped")
plt.xlabel("time (s)")
plt.ylabel("angle (radians)")
for i in range(len(damped_pendulum)):
    if i == 2:
        plt.plot(damped_pendulum[i][0],damped_pendulum[i][1],"g-",label="q=6.1")
    else:    
        plt.plot(damped_pendulum[i][0],damped_pendulum[i][1],"k:")
plt.plot([0,t_end],[0,0],"r-",linewidth=1)
plt.ylim(-0.05,0.2)
plt.legend()
plt.show()
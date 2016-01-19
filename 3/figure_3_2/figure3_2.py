# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:57:07 2016
Simple Pendulum - Euler method
@author: nightwing
"""

from math import pi
import matplotlib.pyplot as plt

g = 9.8               #gravity acceleration (m/s2)
length = 1            #length of the string (m)
k = g / length        #g/length 
t = 0                 #initial time (s)
dt = 0.04             #time step (s)
t_end = 10            #end time (s)
theta = 11.5          #initial angle (degrees)
theta *= (pi/180)     #initial angle (radians)
angular_vel = 0       #initial angular velocity (rad/s) 
angular_velocity = [] #this list store value of angular velocity
angle = []            #this list store value of angle
time = []             #this list store value of time

#-------------caculate (Euler method)------------
while t <= t_end:
    angular_velocity.append(angular_vel)
    angle.append(theta)
    time.append(t)
    angular_vel -= k * theta * dt
    theta += angular_velocity[-1] * dt
    t += dt

#---------------graph----------------
plt.title("Simple Pendulum - Euler method")
plt.xlabel("time (s)")
plt.ylabel("angle (radians)")    
plt.plot(time,angle,"k-")
plt.ylim(-2,2)
plt.show()
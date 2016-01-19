# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:42:32 2016
Simple Pendulum - Euler-Cromer method
@author: nightwing
"""

from math import cos,sqrt,pi
import matplotlib.pyplot as plt

g = 9.8                     #gravity acceleration (m/s2)
mass = 1.0                  #mass of the padulum (kg)
length = 1                  #length of the string (m)
k = g / length              #g/length 
t = 0                       #initial time (s)
dt = 0.04                   #time step (s)
t_end = 10                  #end time (s)
theta = 11.5                #initial angle (degrees)
theta *= (pi/180)           #initial angle (radians)
angular_vel = 0             #initial angular velocity (rad/s) 
angular_velocity = []       #this list store value of angular velocity
angle = []                  #this list store value of angle
time = []                   #this list store value of time
energy = []                 #thie list store value of total energy
cycle = 2*pi*sqrt(length/g) #cycle of the pendulum (s)

#-------------caculate (Euler-Cromer method)------------
while t <= t_end:
    E = 0.5*mass*(length*angular_vel)**2 + mass*g*length*(1-cos(theta))
    energy.append(E)
    angular_velocity.append(angular_vel)
    angle.append(theta)
    time.append(t)
    angular_vel -= k * theta * dt
    theta += angular_vel * dt
    t += dt

#---------------graph----------------
plt.title("Simple Pendulum - Euler-Cromer method")
plt.xlabel("time (s)")
plt.ylabel("total energy (J)")    
plt.plot(time,energy,"k-")
for i in range(int(t_end/cycle)):
    plt.plot([(i+1)*cycle,(i+1)*cycle],[min(energy)*0.9,max(energy)*1.1],"r:")
plt.ylim(min(energy)*0.9,max(energy)*1.1)
plt.show()
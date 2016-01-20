# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:46:05 2016
Simple Pendulum - Euler method
@author: nightwing
"""

from math import cos,pi
import matplotlib.pyplot as plt

g = 9.8                     #gravity acceleration (m/s2)
mass = 1.0                  #mass of the padulum (kg)
length = 1                  #length of the string (m)
k = g / length              #g/length 
t_end = 10                  #end time (s) 
Time = []                   #this list store the list "time"
Energy = []                 #this list store the list "energy" 

#-------------caculate (Euler method)------------
for dt in [0.04, 0.02, 0.01, 0.005]:
    
    t = 0                       #initial time (s)
    theta = 11.5                #initial angle (degrees)
    theta *= (pi/180)           #initial angle (radians)
    angular_vel = 0             #initial angular velocity (rad/s)
    angular_velocity = []       #this list store value of angular velocity
    time = []                   #this list store value of time
    energy = []                 #thie list store value of total energy
    
    while t <= t_end:
        E = 0.5*mass*(length*angular_vel)**2 + mass*g*length*(1-cos(theta))
        energy.append(E)
        angular_velocity.append(angular_vel)
        time.append(t)
        angular_vel -= k * theta * dt
        theta += angular_velocity[-1] * dt
        t += dt
        
    Time.append(time)    
    Energy.append(energy)

#---------------graph----------------
plt.title("Simple Pendulum - Euler method")
plt.xlabel("time (s)")
plt.ylabel("total energy (J)")    
plt.plot(Time[0],Energy[0],"k-",label="dt=0.040s")
plt.plot(Time[1],Energy[1],"k--",label="dt=0.020s")
plt.plot(Time[2],Energy[2],"k-.",label="dt=0.010s")
plt.plot(Time[3],Energy[3],"k:",label="dt=0.005s")
plt.legend(loc=2)
plt.show()
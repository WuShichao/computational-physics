# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:10:42 2016
driven pendulum, using Euler-Cromer method
@author: nightwing
"""

from math import sin,pi
import matplotlib.pyplot as plt

g = 9.8                     #gravity acceleration (m/s2)
length = 1                  #length of the string (m)
k = g / length              #g/length 
dt = 0.04                   #time step (s)
t_end = 20                  #end time (s)
driven_pendulum = []        #this list store time and angle

#caculate driven pendulum
def DRIVEN(Q,F,FRE):            #(q,force,frequency of force) 
    t = 0                       #initial time (s)
    theta = 11.5                #initial angle (degrees)
    theta *= (pi/180)           #initial angle (radians)
    angular_vel = 0             #initial angular velocity (rad/s)
    angle = []                  #this list store value of angle
    time = []                   #this list store value of time

    while t <= t_end:
        angle.append(theta)
        time.append(t)
        angular_vel -= (k*theta + Q*angular_vel - F*sin(FRE*t)) * dt
        theta += angular_vel * dt
        t += dt
    return [time,angle]    
    
#------------------caculate----------------
driven_pendulum.append(DRIVEN(1.0, 0.2, 2.0))

#----------------graph----------------
plt.title("driven pendulum")
plt.xlabel("time (s)")
plt.ylabel("angle (radians)")
plt.plot(driven_pendulum[0][0],driven_pendulum[0][1],"k-",
         label="freq_force=2.0, F=0.2, q=1.0")
plt.ylim(-0.2,0.2)
plt.legend()
plt.show()
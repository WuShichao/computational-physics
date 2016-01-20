# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 19:32:31 2016
Damped pendulum, using Euler-Cromer.
@author: nightwing
"""

from math import pi
import matplotlib.pyplot as plt

g = 9.8                     #gravity acceleration (m/s2)
length = 1                  #length of the string (m)
k = g / length              #g/length 
dt = 0.04                   #time step (s)
t_end = 10                  #end time (s)
damped_pendulum = []        #this list store angle and time 

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
for q in [1,5,10]:
    damped_pendulum.append(DAMPED(q))

#------------------graph------------------    
plt.xlabel("time (s)")
plt.ylabel("angle (radians)")
plt.plot(damped_pendulum[0][0],damped_pendulum[0][1],"k-",label="q=1.0")
plt.plot(damped_pendulum[1][0],damped_pendulum[1][1],"k:",label="q=5")
plt.plot(damped_pendulum[2][0],damped_pendulum[2][1],"k-.",label="q=10")
plt.ylim(-0.2,0.2)
plt.legend()
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:10:42 2016
driven pendulum, displacement resonance
using Euler-Cromer method
@author: nightwing
"""

from numpy import linspace
from math import sin,pi
import matplotlib.pyplot as plt

g = 9.8                     #gravity acceleration (m/s2)
length = 1                  #length of the string (m)
k = g / length              #g/length 
dt = 0.04                   #time step (s)
t_end = 100                 #end time (s)
resonance_amplitude = []    #this list store the resonance amplitude
situations = []             #this list store amplitude of different q

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
        if FRE > 0.1:
            angular_vel -= (k*theta + Q*angular_vel - F*sin(FRE*t)) * dt
        else:
            angular_vel -= (k*theta + Q*angular_vel - F) * dt
        theta += angular_vel * dt
        t += dt

    return [time,angle]    
    
#caculate the resonance amplitude
def RESONANCE_AMPLITUDE(array):
    half = len(array) / 2    #suppose the amplitude become stable
    return max(array[half:-1])
    
#------------------caculate----------------
for q in [1.0, 2.0, 3.0, 4.0]:
    for freq in linspace(0, 6, 100):
        resonance_amplitude.append(RESONANCE_AMPLITUDE(DRIVEN(q,0.2,freq)[1]))
    situations.append(resonance_amplitude)
    resonance_amplitude = []
    
#----------------graph----------------
plt.title("Displacement resonance")
plt.xlabel("driving angular frequency (rad/s)")
plt.ylabel("resonance amplitude (m)")
plt.plot(linspace(0,6,100),situations[0],"r-",label="q=1.0")
plt.plot(linspace(0,6,100),situations[1],"y-",label="q=2.0")
plt.plot(linspace(0,6,100),situations[2],"g-",label="q=3.0")
plt.plot(linspace(0,6,100),situations[3],"b-",label="q=4.0")
plt.legend()
plt.show()
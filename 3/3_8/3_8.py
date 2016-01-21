# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:27:03 2016
correlation of amplitude and peroid (nonlinear pendulum), 
using Euler-Cromer metohd
@author: nightwing
"""
from tqdm import tqdm
from math import sin,pi
from numpy import linspace
import matplotlib.pyplot as plt

g = 9.8               #gravity acceleration (m/s2)
length = 1            #length of the string (m)
k = g / length        #g/length 
dt = 0.0001           #time step (s)
t_end = 20            #end time (s)
correlation = []      #correlation of amplitude and period

#caculate the correlation of amplitude and peroid
def CORRELATION():
    amplitude = []          #this list store the value of amplitude
    peroid = []             #this list store the value of peroid
    for theta in tqdm(linspace(10,90,50)):
        amplitude.append(theta)
        theta *= (pi/180)     #initial angle (radians)
        angular_vel = 0       #initial angular velocity (rad/s) 
        t = 0                 #initial time (s)
        angle = []            #this list store value of angle
        time = []             #this list store value of time
        while t <= t_end:
            angle.append(theta)
            time.append(t)
            angular_vel -= k * sin(theta) * dt
            theta += angular_vel * dt
            t += dt
        #caculate period    
        opposite = -angle[0]
        for i in range(1,len(angle)):
            if abs(angle[i]-opposite) < abs(opposite)*0.001:
                T = time[i] * 2
                break
        peroid.append(T)
    return [amplitude,peroid]    

#---------------caculate-------------------
correlation.append(CORRELATION())

#---------------graph----------------
plt.title("nonlinear pendulum")
plt.xlabel("amplitude (degrees)")
plt.ylabel("peroid (s)")    
plt.plot(correlation[0][0],correlation[0][1],"k-")
plt.show()

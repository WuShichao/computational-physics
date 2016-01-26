# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:55:39 2016
physical pendulum, using Euler-Cromer method
@author: nightwing
"""

from math import sin,pi
import matplotlib.pyplot as plt

g = 9.8               #gravity acceleration (m/s2)
length = 9.8          #length of the rod (m)
k = g / length        #g/length 
dt = 0.04             #time step (s)
t_end = 60            #end time (s)
situations = []       #this list store [time, angle]

#caculate the physical pendulum
def PHYSICAL_PENDULUM(q,fd,freq,theta):
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
    return [time,angle,angular_velocity]
    
#-------------caculate (Euler-Cromer method)------------
for F in [0.1, 0.5, 0.99]:
    situations.append(PHYSICAL_PENDULUM(0.5, F, 2/3.0, 0.2))

#---------------graph----------------
plt.subplot(321)
plt.title("angle versus time(Fd=0.1,0.5,0.99)")
plt.plot(situations[0][0],situations[0][1],"k-")
plt.subplot(323)
plt.ylabel("$\\theta$ (radians)")
plt.plot(situations[1][0],situations[1][1],"k-")
plt.subplot(325)
plt.plot(situations[2][0],situations[2][1],"k-")
plt.xlabel("time (s)")
plt.subplot(322)
plt.title("angular velocity versus time(Fd=0.1,0.5,0.99)")
plt.plot(situations[0][0],situations[0][2],"k-")
plt.subplot(324)
plt.ylabel("$\omega$ (rad/s)")
plt.plot(situations[1][0],situations[1][2],"k-")
plt.subplot(326)
plt.plot(situations[2][0],situations[2][2],"k-")
plt.xlabel("time (s)")
plt.show()
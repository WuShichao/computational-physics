# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:45:32 2016
Study the effects of damping by starting the pendulum with some initial
angular displacement. Using Euler-Cromer method.
@author: nightwing
"""

from math import sin,pi
import matplotlib.pyplot as plt

g = 9.8               #gravity acceleration (m/s2)
length = 9.8          #length of the rod (m)
k = g / length        #g/length 
dt = 0.04             #time step (s)
t_end = 200           #end time (s)
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
for angle in [0.5, 1.0, 1.5]:
    situations.append(PHYSICAL_PENDULUM(0.1, 0, 2/3.0, angle))

#caculate time constant
for situation in range(len(situations)):
    for index in range(len(situations[situation][1])):
        find_time_constant = 'yes'
        for k in range(1000):
            if abs(situations[situation][1][index + k]) > 0.01*abs(situations[situation][1][0]):
                find_time_constant = 'no'
                break
        if find_time_constant == 'yes':
            print "time constant = %.3fs" % situations[situation][0][index]
            break
            
#---------------graph----------------
plt.subplot(311)
plt.title("angle versus time ($\\theta$=0.5, 1.0, 1.5)")
plt.plot(situations[0][0],situations[0][1],"k-",label="$\\theta$=0.5")
plt.legend()
plt.subplot(312)
plt.plot(situations[1][0],situations[1][1],"k-",label="$\\theta$=1.0")
plt.ylabel("angle (radians)")
plt.legend()
plt.subplot(313)
plt.plot(situations[2][0],situations[2][1],"k-",label="$\\theta$=1.5")
plt.xlabel("time (s)")
plt.legend()
plt.show()

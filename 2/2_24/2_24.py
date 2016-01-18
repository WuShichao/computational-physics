# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:15:13 2016
Caculate trajectories of a Ping-Pong ball in different situations.
(topspin and backspin)
Using Eluer method.
@author: nightwing
"""

from math import cos,sin,sqrt,pi
import matplotlib.pyplot as plt

g = 9.8                  #gravity acceleration
density = 1.29           #density of air (kg/m3)
mass = 0.0027            #(kg)
area = 0.00126           #(s2)
initial_velocity = 3.0   #(m/s)
k = 0.04                 #S0/m
angle = 30               #(degrees)
angle *= (pi/180)        #degree to rad
dt = 0.001               #(s)
trajectory = []          #trajectories of several situations

#caculate the trajectory
def TRAJECTORY(w,K0):
    x = 0.0                            #initial x
    y = 0.0                            #initial y
    displacement_x = []                #displacement x
    displacement_y = []                #displacement y
    vx = initial_velocity * cos(angle)
    vy = initial_velocity * sin(angle)
    
    while y >= 0:
        displacement_x.append(x)
        displacement_y.append(y)
        x += vx * dt
        y += vy * dt
        v_net = sqrt(vx**2+vy**2)
        vx += (-0.5*density*area*v_net*vx/mass - K0*w*vy) * dt
        vy += (-0.5*density*area*v_net*vy/mass + K0*w*vx - g) * dt

    trajectory.append([displacement_x,displacement_y])

#--------caculate trajectories----------
for angular_velocity in range(1,11):
    angular_velocity *= (2*pi)
    TRAJECTORY(angular_velocity,k)
for angular_velocity in range(1,11):
    angular_velocity *= (2*pi)
    TRAJECTORY(angular_velocity,-k)
 
#-------------------graph------------------- 
plt.title("Trajectories of a Ping-Pong ball (topspin and backspin)")       
for i in range(len(trajectory)):
    if i < 10:
        plt.plot(trajectory[i][0],trajectory[i][1],"k-")
    else:
        plt.plot(trajectory[i][0],trajectory[i][1],"k--")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend(["backspin"])
plt.show()
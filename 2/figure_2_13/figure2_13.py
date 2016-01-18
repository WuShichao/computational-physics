# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 11:29:31 2016
Caculate the trajectories of the glof in several situations.
Using Euler method.
@author: nightwing
"""

from math import cos,sin,sqrt,pi
import matplotlib.pyplot as plt

g = 9.8                  #gravity acceleration
density = 1.29           #density of air (kg/m3)
mass = 0.046             #(kg)
area = 0.00143           #(s2)
initial_velocity = 70.0  #(m/s)
angle = 9                #(degrees)
angle *= (pi/180)        #degree to rad
dt = 0.01                #(s)
trajectory = []          #trajectories of several situations

#caculate the coefficent C (B2/m)
def C(velocity):
    if velocity <= 14:
        c = 1
    else:
        c = 14.0 / velocity
    return c

#caculate the trajectory
def TRAJECTORY(K,smooth_or_not):
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
        if smooth_or_not == "not smooth":
            vx += (-0.5*C(v_net)*density*area*v_net*vx/mass - K*vy) * dt
            vy += (-0.5*C(v_net)*density*area*v_net*vy/mass + K*vx - g) * dt
        else:
            vx += (-0.5*density*area*v_net*vx/mass - K*vy) * dt
            vy += (-0.5*density*area*v_net*vy/mass + K*vx - g) * dt
    
    trajectory.append([displacement_x,displacement_y])

#--------caculate trajectories--------    
for k in [0, 0.25, 0.25*1.5]:
    TRAJECTORY(k,"not smooth")
TRAJECTORY(0.25,"smooth")

#------------graph------------  
plt.title("Golf ball trajectories")
plt.xlabel("x (m)")
plt.ylabel("y (m)")  
plt.plot(trajectory[0][0],trajectory[0][1],"k-.",label="no spin")
plt.plot(trajectory[1][0],trajectory[1][1],"k-",label="normal drive")
plt.plot(trajectory[2][0],trajectory[2][1],"k:",label="extra backspin")
plt.plot(trajectory[3][0],trajectory[3][1],"k--",label="smooth ball")
plt.xlim(0,300)
plt.ylim(0,80)
plt.legend(loc=1)
plt.show()
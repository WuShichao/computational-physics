# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:38:30 2016
计算棒球飞行轨迹，有C的修正
@author: nightwing
"""

from math import exp,sin,cos,sqrt,pi
import matplotlib.pyplot as plt

g = 9.8           #重力加速度（m/s2）
v = 49.174        #初速度（m/s）  
v_wind = 4.470    #风速（m/s）
angle = 35*pi/180 #出射角度
t = 0             #初始时间（s）
dt = 0.01         #时间间隔 
X = []            #此列表存储x
Y = []            #此列表存储y
trajectory = []   #此列表存储飞行轨迹

#caculate B2/m
def B2M(velocity):
    vd = 35.0
    delta = 5.0
    coefficient = 0.0039 + 0.0058/(1+exp((velocity-vd)/delta))
    return coefficient

#----------欧拉法计算棒球飞行轨迹----------
#no wind
x = 0
y = 0
vx = v * cos(angle)
vy = v * sin(angle)    

while y >= 0:
    X.append(x)
    Y.append(y)
    v_net = sqrt(vx**2+vy**2)
    vx = vx - B2M(v_net)*v_net*vx*dt
    vy = vy - g*dt - B2M(v_net)*v_net*vy*dt
    x += vx * dt
    y += vy * dt    
trajectory.append([X,Y])

#tailwind
x = 0
y = 0
X = []
Y = []
vx = v * cos(angle)
vy = v * sin(angle)    

while y >= 0:
    X.append(x)
    Y.append(y)
    v_net = sqrt((vx-v_wind)**2+vy**2)
    vx = vx - B2M(v_net)*v_net*(vx-v_wind)*dt
    vy = vy - g*dt - B2M(v_net)*v_net*vy*dt
    x += vx * dt
    y += vy * dt    
trajectory.append([X,Y])

#headwind
x = 0
y = 0  
X = []
Y = []
vx = v * cos(angle)
vy = v * sin(angle) 

while y >= 0:
    X.append(x)
    Y.append(y)
    v_net = sqrt((vx+v_wind)**2+vy**2)
    vx = vx - B2M(v_net)*v_net*(vx+v_wind)*dt
    vy = vy - g*dt - B2M(v_net)*v_net*vy*dt
    x += vx * dt
    y += vy * dt    
trajectory.append([X,Y])

#-----------------绘图------------------ 
plt.title("Trajectory of a batted baseball")
plt.xlabel("x (m)")
plt.ylabel("y (m)")   
plt.plot(trajectory[0][0],trajectory[0][1],"g-",label="no wind")
plt.plot(trajectory[1][0],trajectory[1][1],"k-",label="tailwind")
plt.plot(trajectory[2][0],trajectory[2][1],"k--",label="headwind")
plt.legend()
plt.show()   
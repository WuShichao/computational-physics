# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 20:29:42 2016
欧拉法计算恻风对棒球飞行轨迹的影响
@author: nightwing
"""

from math import exp,sin,cos,sqrt,pi
import matplotlib.pyplot as plt

g = 9.8           #重力加速度（m/s2）
v = 49.174        #初速度（m/s）  
v_wind = 4.470    #风速（m/s）
angle = 35*pi/180 #出射角度
dt = 0.01         #时间间隔（s） 
x = 0             #初始x
y = 0             #初始y 
z = 0             #初始z
X = []            #此列表存储x
Y = []            #此列表存储y
Z = []            #此列表存储z

#caculate B2/m
def B2M(velocity):
    vd = 35.0
    delta = 5.0
    coefficient = 0.0039 + 0.0058/(1+exp((velocity-vd)/delta))
    return coefficient

#----------欧拉法计算棒球飞行轨迹----------
vx = v * cos(angle)
vy = v * sin(angle) 
vz = 0.0  

while y >= 0: 
    X.append(x)
    Y.append(y)
    Z.append(z)
    v_net = sqrt(vx**2+vy**2+(vz-v_wind)**2)
    vx = vx - B2M(v_net)*v_net*vx*dt
    vy = vy - g*dt - B2M(v_net)*v_net*vy*dt
    vz = vz - B2M(v_net)*v_net*(vz-v_wind)*dt
    x += vx * dt
    y += vy * dt 
    z += vz * dt

#-----------------绘图------------------ 
plt.title("Effect of the crosswind on a batted baseball")
plt.xlabel("Displacement x (m)")
plt.ylabel("Displacement z (m)")   
plt.plot(X,Z,"k-",label="v_wind = 10mph")
plt.legend(loc=2)
plt.show()   
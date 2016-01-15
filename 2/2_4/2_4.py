# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:39:58 2016
用欧拉法计算自行车上下坡时的速度
@author: nightwing
"""

from math import atan,sin
import matplotlib.pyplot as plt

g = 9.8        #重力加速度(m/s2)
DENSITY = 1.29 #空气密度(kg/m3)
C = 0.5        #阻力系数
A = 0.33       #截面积(m2)
M = 70.0       #人车质量(kg)
v1 = 4.0       #（上坡）速度(m/s)
v2 = 4.0       #（下坡）速度(m/s)
P = 400.0      #功率(w)
t = 0          #初始时间
t_max = 200    #截止时间(s) 
dt = 0.1       #时间间隔
time = []      #此列表存储时间  
velocity1 = [] #此列表存储上坡时的速度
velocity2 = [] #此列表存储下坡时的速度

#---欧拉法计算自行车运动速度---
while t <= t_max:
    velocity1.append(v1)
    velocity2.append(v2)
    time.append(t)
    v1 += P/(M*v1)*dt-C*DENSITY*A*v1**2/(2*M)*dt-g*sin(atan(0.1))*dt
    v2 += P/(M*v2)*dt-C*DENSITY*A*v2**2/(2*M)*dt+g*sin(atan(0.1))*dt
    t += dt    

#------------绘图---------------
plt.title("Bicycling simulation: velocity vs. time")
plt.xlabel("time (s)")
plt.ylabel("velocity (m/s)")
plt.plot(time,velocity1,"k-",label="up")    
plt.plot(time,velocity2,"k--",label="down")
plt.legend(loc=5)
plt.show()
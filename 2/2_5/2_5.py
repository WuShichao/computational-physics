# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:55:48 2016
用欧拉法计算自行车从静止起步后的速度
@author: nightwing
"""

import matplotlib.pyplot as plt

DENSITY = 1.29 #空气密度(kg/m3)
C = 1.0        #阻力系数
A = 0.33       #截面积(m2)
M = 70.0       #人车质量(kg)
v = 7.0        #转折速度(m/s)
v1 = 0.0       #（无阻力）速度(m/s)
v2 = 0.0       #（有阻力）速度(m/s)
P = 400.0      #功率(w)
t = 0          #初始时间
t_max = 200    #截止时间(s) 
dt = 0.1       #时间间隔
time = []      #此列表存储时间  
velocity1 = [] #此列表存储无空气阻力时的速度
velocity2 = [] #此列表存储有空气阻力时的速度

#---欧拉法计算自行车运动速度---
while t <= t_max:
    velocity1.append(v1)
    velocity2.append(v2)
    time.append(t)
    if v1 <= v:
        v1 += P/(M*v)*dt
    if v2 <= v:
        v2 += P/(M*v)*dt-C*DENSITY*A*v2**2/(2*M)*dt
    if v1 > v:
        v1 += P/(M*v1)*dt
    if v2 > v:
        v2 += P/(M*v2)*dt-C*DENSITY*A*v2**2/(2*M)*dt
    t += dt    

#------------绘图---------------
plt.title("Bicycling simulation: velocity vs. time")
plt.xlabel("time (s)")
plt.ylabel("velocity (m/s)")
plt.plot(time,velocity1,"k-",label="No air resistence")    
plt.plot(time,velocity2,"k--",label="With air resistence")
plt.legend(loc=2)
plt.show()
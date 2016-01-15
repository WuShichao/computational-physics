# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 14:39:39 2016
用欧拉法模拟自行车在无空气阻力时的运动
@author: nightwing
"""

from math import sqrt
import matplotlib.pyplot as plt

M = 70.0       #人车质量(kg)
V0 = 4.0       #初始速度(m/s)
v = 4.0        #速度(m/s)
P = 400.0      #功率(w)
t = 0          #初始时间
t_max = 200    #截止时间(s) 
dt = 0.1       #时间间隔
time = []      #此列表存储时间  
velocity1 = [] #此列表存储数值解
velocity2 = [] #此列表存储解析解

#---欧拉法和解析法计算自行车运动速度---
while t <= t_max:
    velocity1.append(v)
    velocity2.append(sqrt(V0**2+2*P*t/M))
    time.append(t)
    v += P/(M*v) * dt
    t += dt    

#------------绘图---------------
plt.title("Bicycling without air resistance")
plt.xlabel("time (s)")
plt.ylabel("velocity (m/s)")
plt.plot(time,velocity2,"r-",label="exact")    
plt.plot(time,velocity1,"k--",label="numerical")
plt.legend(loc=2)
plt.show()
    
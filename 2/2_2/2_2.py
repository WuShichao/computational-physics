# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 16:59:36 2016
用欧拉法计算在相同速度下车队中段比排头节省多少能量
@author: nightwing
"""

import matplotlib.pyplot as plt

DENSITY = 1.29 #空气密度(kg/m3)
C = 0.5        #阻力系数
A = 0.33       #截面积(m2)
M = 70.0       #人车质量(kg)
v1 = 4.0       #排头速度(m/s)
v2 = 4.0       #中段速度(m/s)
P = 400.0      #功率(w)
t = 0          #初始时间
t_max = 200    #截止时间(s) 
dt = 0.1       #时间间隔
time = []      #此列表存储时间  
velocity1 = [] #此列表存储车队排头有空气阻力时的速度
velocity2 = [] #此列表存储车队中段有空气阻力时的速度

#---欧拉法计算自行车运动速度---
while t <= t_max:
    velocity1.append(v1)
    velocity2.append(v2)
    time.append(t)
    v1 += P/(M*v1)*dt-C*DENSITY*A*v1**2/(2*M)*dt
    v2 += 0.7*P/(M*v2)*dt-C*DENSITY*0.7*A*v2**2/(2*M)*dt
    t += dt    

#------------绘图---------------
plt.title("P(middle) / P(front) = 0.7")
plt.xlabel("time (s)")
plt.ylabel("velocity (m/s)")
plt.plot(time,velocity1,"k-",label="front")    
plt.plot(time,velocity2,"k--",label="middle")
plt.legend(loc=4)
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:51:41 2016
用欧拉法模拟自由落体运动
@author: nightwing
"""

import matplotlib.pyplot as plt

g = 9.8       #重力加速度
v = 0         #初始速度
t = 0         #初始时间
dt = 0.01     #时间间隔
t_max = 10    #截止时间
velocity = [] #此列表存储速度
time = []     #此列表存储时间

#-------用欧拉法计算落体速度------
while t <= t_max:
    velocity.append(v)
    time.append(t)
    v -= g * dt
    t += dt

#----------绘图-------------    
plt.title("Free Fall")
plt.xlabel("Time / s")
plt.ylabel("Velocity / m/s")
plt.plot(time, velocity)
plt.show()
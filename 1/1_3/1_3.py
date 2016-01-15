# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:41:53 2016
用欧拉法模拟受空气阻力的落体运动
@author: nightwing
"""

import matplotlib.pyplot as plt

a = 10        #系数a
b = 1         #系数b
v = 0         #初始速度
t = 0         #初始时间
dt = 0.01     #时间间隔
t_max = 10    #截止时间
time = []     #此列表存储时间
velocity = [] #此列表存储速度

#-----欧拉法计算追尾速度------
while t <= t_max:
    time.append(t)
    velocity.append(v)
    v += (a - b*v) * dt
    t += dt
 
#-----------绘图--------------   
plt.title("Terminal Velocity")
plt.xlabel("Time / s")
plt.ylabel("Velocity")
plt.plot(time, velocity)
plt.show()
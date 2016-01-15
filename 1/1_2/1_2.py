# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:02:11 2016
用欧拉法模拟物体的水平运动
@author: nightwing
"""

import matplotlib.pyplot as plt

v = 40.0   #物体初始速度
x = 0.0    #物体初始位置
t = 0      #初始时间
dt = 0.01  #时间间隔
t_max = 10 #截止时间
time = []  #此列表存储时间
posi = []  #此列表存储位移

#---欧拉法计算物体位置----
while t <= t_max:
    posi.append(x)
    time.append(t)
    x += v * dt
    t += dt

#------------绘图-------------    
plt.title("Horizontal Motion")
plt.xlabel("Time / s")
plt.ylabel("Position / m")
plt.plot(time, posi)
plt.show()    
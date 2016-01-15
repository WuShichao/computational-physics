# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:24:25 2016
用欧拉法模拟人口增长
@author: nightwing
"""

import matplotlib.pyplot as plt

N = 100     #初始人口
a = 0.1     #系数a
b = 0.00006 #系数b
t = 0       #初始时间
dt = 1      #时间间隔
t_max = 100 #截止时间
number = [] #此列表存储人口数
time = []   #此列表存储时间

#------欧拉法计算人口变化-------
while t <= t_max:
    number.append(N)
    time.append(t)
    N += (a*N - b*N**2) * dt
    t += dt

#------------绘图--------------
plt.title("Population Growth")
plt.xlabel("Time")
plt.ylabel("Population")
plt.plot(time, number)
plt.show()    


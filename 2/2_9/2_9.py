# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:18:44 2016
在Adiabatic模型下计算炮弹射程和落地动能随发射角度的变化关系
@author: nightwing
"""

from math import cos,sin,sqrt,pi
import matplotlib.pyplot as plt

g = 9.8             #重力加速度（m/s2）
dt = 0.01           #时间间隔（s）
v0 = 700.0          #初始速度（m/s）
k = 4*10**(-5)      #B2/m（m-1）
a = 6.5*10**(-3)    #K/m
alpha = 2.5         #指数
T0 = 300            #海平面处的温度（K）
maximum_range = []  #此列表存储最大射程
Ek = []             #此列表存储炮弹落地时的动能

#-------欧拉法计算炮弹轨迹--------
for theta in range(0,91):
    theta *= (pi/180)    
    t = 0
    x = 0.0
    y = 0.0
    X = []
    Y = []
    vx = v0 * cos(theta)
    vy = v0 * sin(theta)
    while y >= 0:
        v = sqrt(vx**2 + vy**2)
        x += vx * dt
        y += vy * dt
        X.append(x/1000)
        Y.append(y/1000)
        vx -= k*(1-a*y/T0)**alpha*v*vx*dt
        vy -= (g+k*(1-a*y/T0)**alpha*v*vy) * dt
        t += dt
    r = -Y[-2]/Y[-1]
    maximum = (X[-2]+r*X[-1]) / (r+1)
    maximum_range.append(maximum)
    Ek.append((vx**2+vy**2)/100000)
    
#------------------绘图---------------------
plt.subplot(211)
plt.title("Range and Ek of the cannon shell")
plt.ylabel("Range (km)")    
plt.plot(range(0,91),maximum_range,"k-")
plt.subplot(212)
plt.plot(range(0,91),Ek,"k-")
plt.xlabel("Angle (degrees)")
plt.ylabel("Ek (not in SI units)")
plt.show()
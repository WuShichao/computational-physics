# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 14:17:40 2016
欧拉法计算无空气阻力和有空气阻力时炮弹的弹道
@author: nightwing
"""

from math import cos,sin,sqrt,pi
import matplotlib.pyplot as plt

g = 9.8          #重力加速度（m/s2）
dt = 0.01        #时间间隔（s）
v0 = 700.0       #初始速度（m/s）
k = 4*10**(-5)   #B2/m（m-1）
trajectory1 = [] #此列表存储无空气阻力时的弹道
trajectory2 = [] #此列表存储有空气阻力时的弹道

#-------欧拉法计算无空气阻力时的炮弹轨迹--------
for theta in range(30,60,5):
    t = 0
    x = 0.0
    y = 0.0
    displacement_x = []
    displacement_y = []
    theta *= (pi/180)
    vy = v0 * sin(theta)
    while y >= 0:
        displacement_x.append(x/1000)
        displacement_y.append(y/1000)
        x += v0 * cos(theta) * dt
        y += vy * dt
        vy -= g * dt
        t += dt
    trajectory1.append([displacement_x,displacement_y])

#-------欧拉法计算有空气阻力时的炮弹轨迹--------
for theta in range(30,60,5):
    t = 0
    x = 0.0
    y = 0.0
    displacement_x = []
    displacement_y = []
    theta *= (pi/180)
    vx = v0 * cos(theta)
    vy = v0 * sin(theta)
    while y >= 0:
        displacement_x.append(x/1000)
        displacement_y.append(y/1000)
        v = sqrt(vx**2 + vy**2)
        x += vx * dt
        vx -= k*v*vx*dt
        y += vy * dt
        vy -= (g+k*v*vy) * dt
        t += dt       
    trajectory2.append([displacement_x,displacement_y])

#------------------绘图---------------------
plt.subplot(121)
plt.title("Trajectory of cannon shell (No drag)")
plt.xlabel("x (km)")
plt.ylabel("y (km)")    
plt.plot(trajectory1[0][0],trajectory1[0][1],label="30 degrees",color="red")
plt.plot(trajectory1[1][0],trajectory1[1][1],label="35 degrees",color="orange")
plt.plot(trajectory1[2][0],trajectory1[2][1],label="40 degrees",color="yellow")
plt.plot(trajectory1[3][0],trajectory1[3][1],label="45 degrees",color="green")
plt.plot(trajectory1[4][0],trajectory1[4][1],label="50 degrees",color="blue")
plt.plot(trajectory1[5][0],trajectory1[5][1],label="55 degrees",color="purple")
plt.xlim(0,60)
plt.ylim(0,20)

plt.subplot(122)
plt.title("Trajectory of cannon shell (With air drag)")
plt.xlabel("x (km)")
plt.ylabel("y (km)")    
plt.plot(trajectory2[0][0],trajectory2[0][1],label="30 degrees",color="red")
plt.plot(trajectory2[1][0],trajectory2[1][1],label="35 degrees",color="orange")
plt.plot(trajectory2[2][0],trajectory2[2][1],label="40 degrees",color="yellow")
plt.plot(trajectory2[3][0],trajectory2[3][1],label="45 degrees",color="green")
plt.plot(trajectory2[4][0],trajectory2[4][1],label="50 degrees",color="blue")
plt.plot(trajectory2[5][0],trajectory2[5][1],label="55 degrees",color="purple")
plt.xlim(0,60)
plt.ylim(0,20)
plt.legend()

plt.show()
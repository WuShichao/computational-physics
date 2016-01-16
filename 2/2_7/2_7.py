# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 16:15:07 2016
采用空气密度的adiabatic模型，并考虑地表温度随季节的变化
@author: nightwing
"""

from math import cos,sin,sqrt,exp,pi
import matplotlib.pyplot as plt

g = 9.8          #重力加速度（m/s2）
dt = 0.01        #时间间隔（s）
v0 = 700.0       #初始速度（m/s）
k = 4*10**(-5)   #B2/m（m-1）
y0 = 10e4        #y0=kbT/mg（m）
a = 6.5*10**(-3) #K/m
alpha = 2.5      #指数
T0 = 300         #海平面处的温度（K）
trajectory = []  #此列表存储弹道

#-------欧拉法计算炮弹轨迹--------
theta = 45
theta *= (pi/180)

#Without density correction
t = 0
x = 0.0
y = 0.0
displacement_x = []
displacement_y = []
vx = v0 * cos(theta)
vy = v0 * sin(theta)
while y >= 0:
    displacement_x.append(x/1000)
    displacement_y.append(y/1000)
    v = sqrt(vx**2 + vy**2)
    x += vx * dt
    y += vy * dt
    vx -= k*v*vx*dt
    vy -= (g+k*v*vy) * dt
    t += dt       
trajectory.append([displacement_x,displacement_y])

#Isothermal model
t = 0
x = 0.0
y = 0.0
displacement_x = []
displacement_y = []
vx = v0 * cos(theta)
vy = v0 * sin(theta)
while y >= 0:
    displacement_x.append(x/1000)
    displacement_y.append(y/1000)
    v = sqrt(vx**2 + vy**2)
    x += vx * dt
    y += vy * dt
    vx -= k*exp(-y/y0)*v*vx*dt
    vy -= (g+k*exp(-y/y0)*v*vy) * dt
    t += dt    
trajectory.append([displacement_x,displacement_y])

#Adiabatic model (Reference)
t = 0
x = 0.0
y = 0.0
displacement_x = []
displacement_y = []
vx = v0 * cos(theta)
vy = v0 * sin(theta)
while y >= 0:
    displacement_x.append(x/1000)
    displacement_y.append(y/1000)
    v = sqrt(vx**2 + vy**2)
    x += vx * dt
    y += vy * dt
    vx -= k*(1-a*y/T0)**alpha*v*vx*dt
    vy -= (g+k*(1-a*y/T0)**alpha*v*vy) * dt
    t += dt    
trajectory.append([displacement_x,displacement_y])

#Adiabatic model (Winter)
T = 273.15
t = 0
x = 0.0
y = 0.0
displacement_x = []
displacement_y = []
vx = v0 * cos(theta)
vy = v0 * sin(theta)
while y >= 0:
    displacement_x.append(x/1000)
    displacement_y.append(y/1000)
    v = sqrt(vx**2 + vy**2)
    x += vx * dt
    y += vy * dt
    vx -= k*(1-a*y/T0)**alpha*(T/T0)**alpha*v*vx*dt
    vy -= (g+k*(1-a*y/T0)**alpha*(T/T0)**alpha*v*vy) * dt
    t += dt    
trajectory.append([displacement_x,displacement_y])

#Adiabatic model (Summer)
T = 313.15
t = 0
x = 0.0
y = 0.0
displacement_x = []
displacement_y = []
vx = v0 * cos(theta)
vy = v0 * sin(theta)
while y >= 0:
    displacement_x.append(x/1000)
    displacement_y.append(y/1000)
    v = sqrt(vx**2 + vy**2)
    x += vx * dt
    y += vy * dt
    vx -= k*(1-a*y/T0)**alpha*(T/T0)**alpha*v*vx*dt
    vy -= (g+k*(1-a*y/T0)**alpha*(T/T0)**alpha*v*vy) * dt
    t += dt    
trajectory.append([displacement_x,displacement_y])

#------------------绘图---------------------
plt.title("Trajectory of cannon shell")
plt.xlabel("x (km)")
plt.ylabel("y (km)")    
plt.plot(trajectory[0][0],trajectory[0][1],"k--",label="Without density correction")
plt.plot(trajectory[1][0],trajectory[1][1],"k-",label="Isothermal model")
plt.plot(trajectory[2][0],trajectory[2][1],"r--",label="Adiabatic model (Reference)")
plt.plot(trajectory[3][0],trajectory[3][1],"g--",label="Adiabatic model (Winter)")
plt.plot(trajectory[4][0],trajectory[4][1],"g-",label="Adiabatic model (Summer)")
plt.xlim(0,30)
plt.ylim(0,10)
plt.legend()
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 21:33:38 2016
欧拉法计算不同出射角度下飞行指定距离所需的初始速度
@author: nightwing
"""

from tqdm import tqdm
from math import exp,sin,cos,sqrt,pi
import matplotlib.pyplot as plt

g = 9.8               #重力加速度（m/s2）
a = 6.5*10**(-3)      #K/m
alpha = 2.5           #指数
T0 = 300              #海平面处的温度（K）
dt = 0.01             #时间间隔（s） 
target = 167.64       #目标距离（m）
Angle = []            #此列表存储角度  
Velocity = []         #此列表存储击中目标所需的初始速度

#caculate B2/m
def B2M(velocity):
    vd = 35.0
    delta = 5.0
    coefficient = 0.0039 + 0.0058/(1+exp((velocity-vd)/delta))
    return coefficient

#--------------穷举所有情况--------------
for angle in tqdm(range(91)):  
    angle *= (pi/180)
    for v in range(3400):  #精确到0.1m/s，设定速度上限为340.0m/s
        v /= 10.0
        x = 0.0
        y = 0.0
        X = []
        Y = []
        vx = v * cos(angle)
        vy = v * sin(angle)    
        
        while y >= 0:
            X.append(x)
            Y.append(y)
            v_net = sqrt(vx**2+vy**2)
            height = y
            vx = vx - B2M(v_net)*(1-a*height/T0)**alpha*v_net*vx*dt
            vy = vy - g*dt - B2M(v_net)*(1-a*height/T0)**alpha*v_net*vy*dt
            x += vx * dt
            y += vy * dt
    
        if len(X) == 1:
            max_range = 0
        else:
            r = -Y[-2]/Y[-1]
            max_range = (X[-2]+r*X[-1])/(r+1)

        if abs(max_range-target) < 0.5:
            Angle.append(angle/pi*180)
            Velocity.append(v)
            break

#---------------绘图---------------
plt.plot(Angle,Velocity,"k-")
plt.plot([0,90],[49.174,49.174],"r--",label="110mph")
plt.xlabel("Angle (degrees)")
plt.ylabel("Required velocity (m/s)")
plt.legend(loc=2)
plt.show()
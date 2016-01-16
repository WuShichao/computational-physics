# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:38:30 2016
计算棒球飞行轨迹，考虑C的修正和海拔的影响
@author: nightwing
"""

from math import exp,sin,cos,sqrt,pi
import matplotlib.pyplot as plt

g = 9.8               #重力加速度（m/s2）
v = 49.174            #初速度（m/s）  
v_wind = 11.176       #风速（m/s）
a = 6.5*10**(-3)      #K/m
alpha = 2.5           #指数
T0 = 300              #海平面处的温度（K）
t = 0                 #初始时间（s）
dt = 0.01             #时间间隔 
X = []                #此列表存储x
Y = []                #此列表存储y
trajectory = []       #此列表存储飞行轨迹
velocity = []         #此列表存储100mph,45度时的速度
displacement_x = []    #此列表存储100mph,45度时的水平位移
range_baseball_1 = [] #此列表存储no wind时的max_range
range_baseball_2 = [] #此列表存储tailwind时的max_range
range_baseball_3 = [] #此列表存储headwind时的max_range
range_baseball_4 = [] #此列表存储no wind(v=100mph)时的max_range
range_baseball_5 = [] #此列表存储no wind(v=120mph时的max_range

#caculate B2/m
def B2M(velocity):
    vd = 35.0
    delta = 5.0
    coefficient = 0.0039 + 0.0058/(1+exp((velocity-vd)/delta))
    return coefficient

#----------欧拉法计算棒球飞行轨迹----------
#no wind, sea level, max range
for angle in range(91):
    angle *= (pi/180)
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
    range_baseball_1.append(max_range)

#tailwind, sea level, max range
for angle in range(91):
    angle *= (pi/180)
    x = 0
    y = 0
    X = []
    Y = []
    vx = v * cos(angle)
    vy = v * sin(angle)    
    
    while y >= 0:
        X.append(x)
        Y.append(y)
        height = y
        v_net = sqrt((vx-v_wind)**2+vy**2)
        vx = vx - B2M(v_net)*(1-a*height/T0)**alpha*v_net*(vx-v_wind)*dt
        vy = vy - g*dt - B2M(v_net)*(1-a*height/T0)**alpha*v_net*vy*dt
        x += vx * dt
        y += vy * dt
    
    if len(X) == 1:
        max_range = 0
    else:
        r = -Y[-2]/Y[-1]
        max_range = (X[-2]+r*X[-1])/(r+1)
    range_baseball_2.append(max_range)

#headwind, sea level, max range
for angle in range(91):
    angle *= (pi/180)
    x = 0
    y = 0
    X = []
    Y = []
    vx = v * cos(angle)
    vy = v * sin(angle)    
    
    while y >= 0:
        X.append(x)
        Y.append(y)
        height = y
        v_net = sqrt((vx+v_wind)**2+vy**2)
        vx = vx - B2M(v_net)*(1-a*height/T0)**alpha*v_net*(vx+v_wind)*dt
        vy = vy - g*dt - B2M(v_net)*(1-a*height/T0)**alpha*v_net*vy*dt
        x += vx * dt
        y += vy * dt
    
    if len(X) == 1:
        max_range = 0
    else:
        r = -Y[-2]/Y[-1]
        max_range = (X[-2]+r*X[-1])/(r+1)
    range_baseball_3.append(max_range)

#no wind, sea level, max range, v=100mph,120mph
for  i in [10.0/11, 12.0/11]:
    for angle in range(91):
        angle *= (pi/180)
        x = 0.0
        y = 0.0
        X = []
        Y = []
        vx = v * i * cos(angle)
        vy = v * i * sin(angle)    
        
        while y >= 0:
            X.append(x)
            Y.append(y)
            v_net = sqrt(vx**2+vy**2)
            if i == 10.0/11 and angle == pi/4:
                velocity.append(v_net)
                displacement_x.append(x)
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
            
        if i == 10.0/11:
            range_baseball_4.append(max_range)
        else:
            range_baseball_5.append(max_range)

#-----------------绘图------------------ 
plt.subplot(221)
plt.xlabel("Angle (degrees)")
plt.ylabel("Range (m)")   
plt.plot(range(91),range_baseball_1,"k-",label="no wind")
plt.plot(range(91),range_baseball_2,"g-",label="tailwind")
plt.plot(range(91),range_baseball_3,"g--",label="headwind")
plt.legend(loc=8)
plt.subplot(222)
plt.xlabel("Angle (degrees)")
plt.ylabel("Range (m)")
plt.plot(range(91),range_baseball_1,"r-",label="v=110mph")
plt.plot(range(91),range_baseball_4,"k-",label="v=100mph")
plt.plot(range(91),range_baseball_5,"k--",label="v=120mph")
plt.legend(loc=8)
plt.subplot(212)
plt.plot(displacement_x,velocity,"k-")
plt.xlabel("Displacement x (m)")
plt.ylabel("Velocity (m/s)")
plt.xlim(0,max(displacement_x))
plt.ylim(0,max(velocity))
plt.show()   
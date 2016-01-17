# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 15:24:03 2016
计算knuckleball飞行轨迹与初相位、角速度和初速度的关系
@author: nightwing
"""

from math import cos,sin,exp,sqrt,pi
import matplotlib.pyplot as plt

g = 9.8                   #重力加速度（m/s2）
velocity = 29.0576        #初速度（m/s）
angle_velocity = 0.2*2*pi #角速度（rad/s）
dt = 0.01                 #时间间隔（s）
trajectory = []           #此列表存储飞行轨迹

#caculate B2/m
def B2_M(velocity):
    vd = 35.0
    delta = 5.0
    coefficient = 0.0039 + 0.0058/(1+exp((velocity-vd)/delta))
    return coefficient
    
#caculate F(lateral)/(mg)    
def FORCE_MG(theta):
    return 0.5*(sin(4*theta)-0.25*sin(8*theta)+
           0.08*sin(12*theta)-0.025*sin(16*theta))
 
#---------------欧拉法计算飞行轨迹-------------- 
angle = 10               #投掷角度（degrees）
angle *= (pi/180)        #转换为弧度制 

for orientation in range(0,360):
    
    orientation *= (pi/180)    #初相位
    alpha = orientation        #转角
    x = 0.0
    y = 0.0
    z = 0.0
    displacement_x = []
    displacement_y = []
    displacement_z = []
    vx = velocity * cos(angle)
    vy = velocity * sin(angle)
    vz = 0.0
    
    while y >= 0:
        displacement_x.append(x)
        displacement_y.append(y)
        displacement_z.append(z)
        alpha += angle_velocity * dt
        x += vx * dt
        y += vy * dt
        z += vz * dt
        v_net = sqrt(vx**2+vy**2+vz**2)
        vx = vx - B2_M(v_net)*v_net*vx*dt
        vy -= g * dt
        vz += FORCE_MG(alpha)*g*dt
    
    trajectory.append([displacement_x,displacement_z])

#------------------绘图----------------
for i in range(len(trajectory)):
    plt.plot(trajectory[i][0],trajectory[i][1],"k-")
plt.xlabel("x (m)")
plt.ylabel("z (m)")
plt.show()        
           
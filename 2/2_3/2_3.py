# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:11:44 2016
考虑空气阻力的斯托克斯项
@author: nightwing
"""

import matplotlib.pyplot as plt

DENSITY1 = 1.29    #空气密度(kg/m3)
DENSITY2 = 1000.0  #水的密度(kg/m3)
C = 0.5            #阻力系数
n1 = 2e-5          #空气粘滞系数(Pa*s)
n2 = 1e-3          #水的粘滞系数(Pa*s)
H = 1.6            #人车高度(m)
A = 0.33           #截面积(m2)
M = 70.0           #人车质量(kg)
v1 = 4.0           #空气中的速度(m/s)
v2 = 4.0           #空气中（不考虑粘滞阻力）的速度(m/s)
v3 = 4.0           #水中的速度(m/s)
P = 400.0          #功率(w)
t = 0              #初始时间(s)
t_max = 200        #截止时间(s) 
dt = 0.1           #时间间隔(s)
time = []          #此列表存储时间  
velocity1 = []     #此列表存储空气中的速度
velocity2 = []     #此列表存储空气中（无粘滞阻力）的速度
velocity3 = []     #此列表存储水中的速度

#---欧拉法计算自行车运动速度---
while t <= t_max:
    velocity1.append(v1)
    velocity2.append(v2)
    velocity3.append(v3)
    time.append(t)
    v1 += P/(M*v1)*dt-n1*A*v1/H-C*DENSITY1*A*v1**2/(2*M)*dt
    v2 += P/(M*v2)*dt-C*DENSITY1*A*v2**2/(2*M)*dt
    v3 += P/(M*v3)*dt-n2*A*v3/H-C*DENSITY2*A*v3**2/(2*M)*dt
    t += dt    

#------------绘图---------------
plt.title("the effect of the Stokes term")
plt.xlabel("time (s)")
plt.ylabel("velocity (m/s)")
plt.plot(time,velocity1,"k-",label="air")    
plt.plot(time,velocity2,"k--",label="air(no viscous drag)")
plt.plot(time,velocity3,"b--",label="water")
plt.legend(loc=5)
plt.show()
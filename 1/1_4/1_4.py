# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 21:49:13 2015
通过欧拉法模拟两种原子（一种可衰变为另一种）的衰变情况
@author: nightwing
"""

import matplotlib.pyplot as plt

k = float(raw_input("A和B的半衰期之比："))
NA = 10000           #A原子初始数量
NB = 10000           #B原子初始数量
TAU_B = 100          #B原子半衰期  
TAU_A = TAU_B * k    #A原子半衰期
t = 1                #初始时间                                                                 
dt = 0.01            #时间间隔
t_max = 1000         #截止时间
n_a = []             #此列表存储A原子的数量    
n_b = []             #此列表存储B原子的数量
T = []               #此列表存储时间

#-------用欧拉法求解两个相互关联的常微分方程------
while t <= t_max:    
    T.append(t)
    n_a.append(NA)
    n_b.append(NB)
    NA -= NA / TAU_A * dt
    NB += (NA/TAU_A - NB/TAU_B) * dt    
    t += dt

#----------------绘图-----------------    
plt.plot(T, n_a, label="A", color="red")
plt.plot(T, n_b, label="B", color="black")
plt.title("Ta / Tb = %.3f" % k)
plt.ylabel("Number of Nuclei")
plt.xlabel("Time / s")
plt.legend()
plt.show()




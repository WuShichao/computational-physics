# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:15:34 2016
从1749年1月开始每月的太阳黑子数（取前1000组数据）
@author: nightwing
"""

from numpy import loadtxt
import matplotlib.pyplot as plt

def average_sunspots(spots):
    r = 5.0
    return sum(spots)/(2*r)

data = loadtxt("sunspots.txt",float)
month = data[:,0]
number = data[:,1]
ave_sunspots = []

for i in range(1000):
    if (i-5) % 11 == 0:
        ave_sunspots.append(average_sunspots(number[i-5:i+5]))

plt.subplot(211)
plt.title("sunspots")
plt.xlabel("month")  
plt.ylabel("number")
plt.plot(month[:1000],number[:1000],"k-") 
plt.subplot(212)   
plt.plot(range(len(ave_sunspots)),ave_sunspots,"k-")  
plt.xlabel("year")
plt.ylabel("number")
plt.show()

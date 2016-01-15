# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 13:15:42 2015
Hertzsprung–Russell Diagram
@author: nightwing
"""

from numpy import loadtxt,array
import matplotlib.pyplot as plt

data = loadtxt("stars.txt", float)
x = data[:,0]
y = data[:,1]
Lx = array([3500,3500])
Ly = array([-5,20])

plt.scatter(x, y, color="black", s=5)
plt.plot(Lx, Ly,"g--")
plt.title("HR Diagram")
plt.xlabel("Temperature / K")
plt.ylabel("Magnitude")
plt.xlim(16000, 0)
plt.ylim(20, -5)
plt.show()

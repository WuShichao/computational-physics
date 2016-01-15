# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:13:29 2016
用imshow()函数绘制硅原子图像
@author: nightwing
"""

from numpy import loadtxt
import matplotlib.pyplot as plt

data = loadtxt("stm.txt", float)
plt.imshow(data, origin="lower")
plt.colorbar()
plt.gray()
plt.show()
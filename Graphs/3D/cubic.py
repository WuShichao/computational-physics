# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 21:05:02 2016
简单立方堆积
@author: nightwing
"""

from visual import sphere

L = 5
R = 0.3

for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            sphere(pos=[i,j,k], radius=R)
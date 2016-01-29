# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 20:46:05 2016
Caculate the bifurcation diagram for the logistic map.
@author: nightwing
"""

from tqdm import tqdm
from numpy import linspace
import matplotlib.pyplot as plt

situations = [] #this list store [u,value_x]

#caculate x and n at different u
def LOGISTIC_MAP(x,u):
    n = 1           #initial value of n 
    n_end = 100     #end of n 
    value_x = []    #this list store the value of x
    
    while n <= n_end:
        if n >= 30:
            value_x.append(x)
        x = u*x*(1-x)
        n += 1
    return [value_x]

#-----------caculate-------------    
AMOUNTS = 1000
range_mu = linspace(0,4,AMOUNTS)

for mu in tqdm(range_mu):
    situations.append(LOGISTIC_MAP(0.5,mu))
  
#----------------graph--------------
plt.title("Bifurcation diagram  $x$ versus $\mu$")
plt.xlabel("$\mu$")
plt.ylabel("$x$")
for i in range(AMOUNTS):
    MU = [range_mu[i]]
    for X in situations[i]:
        plt.scatter(MU*len(X),X,s=1)
plt.xlim(0,4)
plt.ylim(0,1)        
plt.show()

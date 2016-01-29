# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:39:29 2016
Behavior of x as a functions of n for the logistic map.
@author: nightwing
"""

import matplotlib.pyplot as plt

situations = [] #this list store [value_n,value_x]

#caculate x and n at different u
def LOGISTIC_MAP(x,u):
    n = 1           #initial value of n 
    n_end = 50      #end of n 
    value_n = []    #this list store the value of n
    value_x = []    #this list store the value of x    
    while n <= n_end:
        value_n.append(n)
        value_x.append(x)
        x = u*x*(1-x)
        n += 1
    return [value_n,value_x]

#---------caculate----------
for u in [2.0, 3.1, 3.8]:
    if u == 3.1:
        situations.append(LOGISTIC_MAP(0.6, u))
    else:
        situations.append(LOGISTIC_MAP(0.3, u))

#----------graph-----------
plt.subplot(121)
plt.title("logistic map  x vs n")    
plt.xlabel("n")
plt.ylabel("x")
plt.scatter(situations[0][0],situations[0][1],color="black")
plt.plot(situations[0][0],situations[0][1],"k-")
plt.text(20,0.4,r'$\mu$ = 2.0')
plt.scatter(situations[1][0],situations[1][1],color="black")
plt.plot(situations[1][0],situations[1][1],"k-")
plt.text(20,0.8,r'$\mu$ = 3.1')
plt.xlim(0,50)
plt.ylim(0,1)
plt.subplot(122)
plt.title("logistic map  x vs n")
plt.xlabel("n")
plt.ylabel("x")
plt.scatter(situations[2][0],situations[2][1],color="black")
plt.plot(situations[2][0],situations[2][1],"k-")
plt.text(20,0.1,r'$\mu$ = 3.8')
plt.xlim(0,50)
plt.ylim(0,1)
plt.show()    
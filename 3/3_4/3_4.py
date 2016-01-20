# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 12:05:17 2016
Pandulum:relationship between amplitude and peroid 
(harmonic and anharmonic)
Euler-Cromer method
@author: nightwing
"""

from numpy import linspace
import matplotlib.pyplot as plt

k = 1            #coefficient k
t_end = 50       #end of time
dt = 0.01        #time step
correlation = [] #correlation of amplitude and period

#caculate the correlation of amplitude and peroid
def CORRELATION(ALPHA):
    amplitude = []          #this list store the value of amplitude
    peroid = []             #this list store the value of peroid
    for x in linspace(0.2, 1.0, 50):
        #caculate displacement
        y = 0.0             #initial y
        t = 0               #initial t  
        displacement = []   #this list store the value of x 
        time = []           #this list store the value of time
        amplitude.append(x)
        while t <= t_end:
            displacement.append(x)
            time.append(t)
            y -= k*x**ALPHA * dt
            x += y * dt
            t += dt
        #caculate period    
        opposite = -displacement[0]
        for i in range(1,len(displacement)):
            if abs(displacement[i] - opposite) < abs(opposite)*0.01:
                T = time[i] * 2
                break
        peroid.append(T)
    return [amplitude,peroid]

#---------------caculate-------------------
for  alpha in [1,3]:
    correlation.append(CORRELATION(alpha))
  
#---------------graph------------------
plt.subplot(121)
plt.title("harmonic")  
plt.xlabel("Amplitude")
plt.ylabel("Peroid")  
plt.plot(correlation[0][0],correlation[0][1],"k-")
plt.subplot(122)
plt.title("anharmonic")
plt.xlabel("Amplitude")
plt.ylabel("Peroid")
plt.plot(correlation[1][0],correlation[1][1],"k-")
plt.show()    
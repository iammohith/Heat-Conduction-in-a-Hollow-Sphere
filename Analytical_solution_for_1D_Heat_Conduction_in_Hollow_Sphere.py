# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:09:11 2020

@author: Mohith Sai
"""
""" Let us consider a Hollow sphere with inner and outer radius as
Ri and Ro & the inner temperature Ti and outer temperature To & heat flow is radially
then the temperature distribution is given by
T(r) = (To - Ti)*(Ro/(Ro - Ri))*(1 - (Ri/r)) + Ti"""

import numpy as np
import matplotlib.pyplot as plt

Ti = 100 #inside sphere temperature units must be in degC
To = 20 #outside sphere temperature units must be in degC
Ri = 0.5 #inside radius of sphere units must be in meters
Ro = 1 #outside radius of sphere units must be in meters
n = 20 #the number of points
r = np.linspace(Ri,Ro,n) #linearlyspaced points
T = np.ones(n) #preallocating array of ones for temperature
for i in range(0,n):
    T[i] = ((To - Ti)*(Ro/(Ro - Ri))*(1 - (Ri/r[i]))) + Ti
plt.figure(1)
plt.plot(r,T,color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distacnce (m)')
plt.ylabel('Temperature (C)')
plt.title('Temperature Graph')
print("The temperatures are:",T)

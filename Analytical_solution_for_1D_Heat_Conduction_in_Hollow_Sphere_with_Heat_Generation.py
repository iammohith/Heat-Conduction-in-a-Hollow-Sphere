# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:23:51 2020

@author: Mohith Sai
"""
""" Let us consider a Hollow sphere with inner and outer radius as
Ri and Ro &  for simpilicity we are assuming the inner temperature and outer temperature 
same Tw & heat flow is radially with heat generation Qg with thermal conducutivity k 
then the temperature distribution is given by
T(r) = Tw + Qg/6*k*(Ro**2 - r**2) + (Qg*Ri**3/3*k)*((1/Ro) - (1/r)) """

import numpy as np
import matplotlib.pyplot as plt

Tw = 100 #outside sphere temperature units must be in degC
Ri = 0.5 #inside radius of sphere units must be in meters
Ro = 1 #outside radius of sphere units must be in meters
Qg = 100 #heat generation the units must be W/m**3
K = 10 #thermal conductivity of the material
n = 20 #the number of points
r = np.linspace(Ri,Ro,n) #linearlyspaced points
T = np.ones(n) #preallocating array of ones for temperature
const = const = Qg/6*K
for i in range(0,n):
    T[i] = Tw + (const*((Ro**2) - (r[i]**2))) + ((2*const*Ri**3)*((1/Ro) - (1/r[i])))
plt.figure(1)
plt.plot(r,T,color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distacnce (m)')
plt.ylabel('Temperature (C)')
plt.title('Axisymmetrical Temperature Graph')
print("The temperatures are:",T)

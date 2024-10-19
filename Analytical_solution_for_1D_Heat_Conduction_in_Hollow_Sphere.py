# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:09:11 2020

@author: Mohith Sai
"""
"""
This script calculates and visualizes the temperature distribution 
in a hollow sphere. The heat flow is assumed to be radial, with 
inner and outer radii \( R_i \) and \( R_o \) and corresponding 
inner and outer temperatures \( T_i \) and \( T_o \).

The temperature distribution is given by the equation:

\[
T(r) = (T_o - T_i) \cdot \left(\frac{R_o}{R_o - R_i}\right) \cdot \left(1 - \frac{R_i}{r}\right) + T_i
\]

Where:
- \( T(r) \): temperature at radius \( r \)
- \( R_i \): inner radius of the sphere (in meters)
- \( R_o \): outer radius of the sphere (in meters)
- \( T_i \): inner temperature of the sphere (in °C)
- \( T_o \): outer temperature of the sphere (in °C)
- \( n \): number of points to evaluate
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the hollow sphere
Ti = 100  # Inner sphere temperature (°C)
To = 20   # Outer sphere temperature (°C)
Ri = 0.5  # Inner radius (m)
Ro = 1    # Outer radius (m)
n = 20    # Number of discrete points for temperature calculation

# Create an array of radii from Ri to Ro
r = np.linspace(Ri, Ro, n)  # Linearly spaced points

# Preallocate an array for temperature values
T = np.ones(n)  # Initialize temperature array

# Calculate temperature distribution for each radius
for i in range(n):
    T[i] = ((To - Ti) * (Ro / (Ro - Ri)) * (1 - (Ri / r[i]))) + Ti

# Plot the temperature distribution
plt.figure(1)
plt.plot(r, T, color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution in a Hollow Sphere')
plt.grid()  # Add grid for better readability
plt.show()  # Display the plot

# Print the temperature values for each radius
print("The temperatures at various points are:", T)

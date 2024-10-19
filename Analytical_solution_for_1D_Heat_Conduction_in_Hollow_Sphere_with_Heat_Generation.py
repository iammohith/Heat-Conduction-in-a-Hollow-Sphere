# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:23:51 2020

@author: Mohith Sai
"""
"""
This script calculates and visualizes the temperature distribution 
in a hollow sphere with radial heat flow and heat generation. 
For simplicity, it is assumed that the inner and outer temperatures 
are the same (\( T_w \)), and the temperature distribution is influenced by 
the heat generation rate (\( Q_g \)) and thermal conductivity (\( k \)).

The temperature distribution is given by the equation:

\[
T(r) = T_w + \frac{Q_g}{6k}(R_o^2 - r^2) + \left(\frac{Q_g R_i^3}{3k}\right)\left(\frac{1}{R_o} - \frac{1}{r}\right)
\]

Where:
- \( T(r) \): Temperature at radius \( r \)
- \( T_w \): Uniform temperature at the inner and outer surfaces (in °C)
- \( R_i \): Inner radius of the sphere (in meters)
- \( R_o \): Outer radius of the sphere (in meters)
- \( Q_g \): Heat generation rate (in W/m³)
- \( k \): Thermal conductivity of the material
- \( n \): Number of discrete points for temperature calculation
"""

import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the hollow sphere
Tw = 100  # Temperature (°C) at the inner and outer surfaces
Ri = 0.5  # Inner radius (m)
Ro = 1    # Outer radius (m)
Qg = 100  # Heat generation rate (W/m³)
K = 10    # Thermal conductivity (W/(m·K))
n = 20    # Number of discrete points for temperature calculation

# Create an array of radii from Ri to Ro
r = np.linspace(Ri, Ro, n)  # Linearly spaced points

# Preallocate an array for temperature values
T = np.ones(n)  # Initialize temperature array

# Calculate the constant factor for temperature distribution
const = Qg / (6 * K)

# Calculate temperature distribution for each radius
for i in range(n):
    T[i] = Tw + (const * (Ro**2 - r[i]**2)) + ((Qg * Ri**3 / (3 * K)) * ((1 / Ro) - (1 / r[i])))

# Plot the temperature distribution
plt.figure(1)
plt.plot(r, T, color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution in a Hollow Sphere with Heat Generation')
plt.grid()  # Add grid for better readability
plt.show()  # Display the plot

# Print the temperature values for each radius
print("The temperatures at various points are:", T)

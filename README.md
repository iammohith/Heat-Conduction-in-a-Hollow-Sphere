# Heat Conduction in a Hollow Sphere

This repository contains Python code for simulating heat conduction in a hollow sphere with radial heat flow, heat generation, and varying thermal properties. The temperature distribution is calculated based on the governing equations of heat conduction.

## Project Overview

This project explores the thermal behavior of a hollow sphere characterized by its inner radius $R_i$, outer radius $R_o$, inner temperature $T_i$, and outer temperature $T_o$. The temperature distribution within the sphere is influenced by heat generation $Q_g$ and the thermal conductivity $k$ of the material.

### Key Features:
- Calculates the temperature distribution in a hollow sphere with radial heat flow.
- Accounts for uniform heat generation within the material.
- Visualizes temperature profiles using Python's `matplotlib` library.

## Formulas Used

### 1. **Temperature Distribution with Same Inner and Outer Temperatures**

The temperature distribution for a hollow sphere where the inner and outer temperatures are the same is given by:

$$
T(r) = T_w + \frac{Q_g}{6k}(R_o^2 - r^2) + \left(\frac{Q_g R_i^3}{3k}\right)\left(\frac{1}{R_o} - \frac{1}{r}\right)
$$

Where:
- $T(r)$ is the temperature at a distance $r$ from the center of the sphere.
- $T_w$ is the uniform temperature at the inner and outer surfaces.
- $R_i$ is the inner radius of the sphere.
- $R_o$ is the outer radius of the sphere.
- $Q_g$ is the rate of heat generation per unit volume.
- $k$ is the thermal conductivity of the material.

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/iammohith/Heat-Conduction-in-a-Hollow-Sphere.git
   
2. **Install dependencies**:
   Make sure you have Python installed, and then install the required packages:
   ```bash
   pip install numpy matplotlib
   ```

3. **Run the simulations**:
   The Python scripts simulate heat conduction through the hollow sphere. To run a script, execute:
   ```bash
   python script_name.py
   ```

4. **Modify Parameters**:
   You can change parameters such as $T_w$, $R_i$, $R_o$, $Q_g$, and $k$ in the scripts to test different thermal scenarios.

## Visualizations

The temperature distributions are plotted using `matplotlib`. Each script generates a plot showing the temperature across the hollow sphere. Here's an example of a typical temperature distribution graph:
- **X-axis**: Distance from the center of the sphere.
- **Y-axis**: Temperature at that distance.

## References

1. **Heat and Mass Transfer: Fundamentals & Applications**  
   *Afshin J. Ghajar and Yunus A Çengel*

2. **Heat and Mass Transfer**  
   *R.K. Rajput*

3. **Python Documentation**  
   Official Python documentation for libraries like `numpy` and `matplotlib`:  
   [Python Documentation](https://docs.python.org/3/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

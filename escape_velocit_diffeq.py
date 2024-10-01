# Joey Garcia
# Escape Velocity Application
# Purpose: Determine solution using differential equation. 

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24     # Mass of Earth (kg)
R = 6350e3       # Radius of Earth (m)
g = 127008 / (3600**2)  # Convert acceleration (km/hr^2 to m/s^2)

# Define the differential equation
def equations(t, y):
    x, v = y
    dxdt = v
    dvdt = -G * M / (R + x)**2
    return [dxdt, dvdt]

# Initial conditions
x0 = 0  # Starting at Earth's surface (x = 0)
v0 = np.sqrt(2 * G * M / R)  # Estimate of escape velocity

# Time span for the simulation (in seconds)
t_span = (0, 5000)  # Time span
y0 = [x0, v0]  # Initial position and velocity

# Solving the differential equation using solve_ivp (Runge-Kutta method)
solution = solve_ivp(equations, t_span, y0, method='RK45', dense_output=True)

# Extract results
t_vals = solution.t
x_vals, v_vals = solution.y

# Plotting the results
plt.figure(figsize=(10,6))
plt.plot(t_vals, x_vals / 1000)  # Convert to kilometers
plt.title('Height vs Time for Object with Escape Velocity')
plt.xlabel('Time (seconds)')
plt.ylabel('Height (km)')
plt.grid(True)
plt.show()

# Display escape velocity
v0_kmh = v0 * 3.6  # Convert m/s to km/h
print("Initial Velocity v_0:")
print(v0_kmh)

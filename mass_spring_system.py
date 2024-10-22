import numpy as np
import matplotlib.pyplot as plt

# Define time range
t = np.linspace(0, 10, 1000)

# Transient solution
transient = np.exp(-t) * np.sin(2 * t)

# Steady-state solution
steady_state = np.sin(3 * t) - np.cos(3 * t)

# Total solution
total_solution = transient + steady_state

# Plot the solutions
plt.figure(figsize=(10, 6))
plt.plot(t, transient, label="Transient Solution (e^(-t)sin(2t))", linestyle="--", color="blue")
plt.plot(t, steady_state, label="Steady-State Solution (sin(3t) - cos(3t))", linestyle="--", color="green")
plt.plot(t, total_solution, label="Total Solution", color="red")

plt.title("Mass-Spring System: Transient and Steady-State Solutions")
plt.xlabel("Time (t)")
plt.ylabel("y(t)")
plt.legend()
plt.grid(True)
plt.show()

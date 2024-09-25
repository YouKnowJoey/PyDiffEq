import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the differential equation dy/dx = -2y
def dydx(t, y):
    return -2 * y

# Initial condition y(0) = 1
y0 = [1]

# Time points where we want the solution
t = np.linspace(0, 5, 100)

# Solve the differential equation using solve_ivp
sol = solve_ivp(dydx, [t[0], t[-1]], y0, t_eval=t)

# Plot the solution
plt.plot(sol.t, sol.y[0], label='y(t)')
plt.xlabel('t')
plt.ylabel('y')
plt.title("Solution of dy/dx = -2y")
plt.legend()
plt.grid(True)
plt.show()

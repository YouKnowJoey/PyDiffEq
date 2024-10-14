import numpy as np
import matplotlib.pyplot as plt

def rk4(f, y0, t0, t_end, h):
    """
    Runge-Kutta 4th order method for solving ODEs.
    
    Parameters:
    f: function defining the ODE (dy/dt = f(t, y))
    y0: initial value of y
    t0: initial time
    t_end: final time
    h: step size
    
    Returns:
    t_values: array of time values
    y_values: array of corresponding y values
    """
    # Number of steps
    n_steps = int((t_end - t0) / h) + 1
    t_values = np.linspace(t0, t_end, n_steps)
    y_values = np.zeros(n_steps)
    y_values[0] = y0

    for n in range(0, n_steps - 1):
        k1 = f(t_values[n], y_values[n])
        k2 = f(t_values[n] + h / 2, y_values[n] + h * k1 / 2)
        k3 = f(t_values[n] + h / 2, y_values[n] + h * k2 / 2)
        k4 = f(t_values[n] + h, y_values[n] + h * k3)

        y_values[n + 1] = y_values[n] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    return t_values, y_values

# Define the ODE
def ode_function(t, y):
    return t + y  # dy/dt = t + y

# Parameters
y0 = 1         # Initial condition y(0) = 1
t0 = 0         # Start time
t_end = 1      # End time
h = 0.1        # Step size

# Solve the ODE
t_values, y_values = rk4(ode_function, y0, t0, t_end, h)

# Plotting the results
plt.plot(t_values, y_values, label="RK4 Solution", marker='o')
plt.title("Runge-Kutta 4th Order Method")
plt.xlabel("Time (t)")
plt.ylabel("y(t)")
plt.grid()
plt.legend()
plt.show()

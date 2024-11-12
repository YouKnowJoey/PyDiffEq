import numpy as np
import matplotlib.pyplot as plt

def system_one():
    # Define the system of equations
    def f(x, y):
        return (y - x) * (y - 1)

    def g(x, y):
        return (x - y) * (x - 1)

    # Create a grid of points
    x_vals = np.linspace(-1, 2, 20)
    y_vals = np.linspace(-1, 2, 20)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Compute derivatives
    DX = f(X, Y)
    DY = g(X, Y)

    # Normalize the arrows for better visibility
    M = (np.hypot(DX, DY))
    M[ M == 0] = 1.  # avoid zero division
    DX /= M
    DY /= M

    # Create the phase plane diagram
    plt.figure(figsize=(10, 8))
    plt.quiver(X, Y, DX, DY, color='b', headlength=3)
    plt.title('Phase Plane Diagram')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-1, 2)
    plt.ylim(-1, 2)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid()
    plt.show()

def system_two():
    # Define the vector field for the system
    def dx_dt(x, y):
        return -y * (y - 2)

    def dy_dt(x, y):
        return (x - 1) * (y - 1)

    # Create a grid of points
    x_values = np.linspace(-2, 3, 20)
    y_values = np.linspace(-2, 3, 20)
    X, Y = np.meshgrid(x_values, y_values)

    # Compute the direction field (dx, dy) at each point
    U = dx_dt(X, Y)
    V = dy_dt(X, Y)

    # Plotting
    plt.figure(figsize=(8, 8))
    plt.quiver(X, Y, U, V, color="blue")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Phase Plane Diagram for the System:\n dx/dt = -y(y-2), dy/dt = (x-1)(y-1)")
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.show()

system_two()
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Function, diff, summation, series


# Define the symbols and functions
x, n = symbols('x n') 
a = symbols('a', cls=Function)

# Define the power series expansion for y
y_series = summation(a(n) * x**n, (n, 0, 6))  # up to x^6 to ensure enough terms

print("y_series: ", y_series)

# Compute y' and y''
y_prime_series = diff(y_series, x)
y_double_prime_series = diff(y_prime_series, x)

print("y_prime_series: ", y_prime_series)
print("y_double_prime_series: ", y_double_prime_series)

# Set up the differential equation
lhs = (2*x - 3) * y_double_prime_series - x * y_prime_series + y_series
lhs_expanded = lhs.series(x, 0, 6).removeO()  # Expanding around x=0 up to x^6

print("Left-handside expanded: ", lhs_expanded)


def plot_power_series():
    # Define coefficients found from power series expansion
    a0 = 0   # From y(0) = 0
    a1 = 1   # From y'(0) = 1

    # Calculated terms manually (results from step-by-step substitution)
    a2 = 0
    a3 = -1/3
    a4 = 0
    a5 = 1/15

    # Define the polynomial function using the first five nonzero terms
    def y_polynomial(x):
        return a0 + a1 * x + a2 * x**2 + a3 * x**3 + a4 * x**4 + a5 * x**5

    # Create x values for plotting on the interval (-10, 10)
    x_values = np.linspace(-10, 10, 400)
    y_values = y_polynomial(x_values)

    # Plotting the resulting polynomial
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label="Approximate Solution (Power Series)")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.title("Approximate Solution to 2y'' + xy' + y = 0 using Power Series Expansion")
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.legend()
    plt.grid(True)
    plt.show()

plot_power_series()
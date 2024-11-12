import numpy as np

# Define the function for Euler's Method
def f(t, x):
    return 1 + t * np.sin(t * x)

# Initial conditions and parameters
t0 = 0      # Initial time
x0 = 0      # Initial value of x
t_end = 1   # End value of t
n_steps = 10  # Number of steps
h = (t_end - t0) / n_steps  # Step size

# Arrays to store values of t and x
t_values = np.linspace(t0, t_end, n_steps + 1)
x_values = np.zeros(n_steps + 1)
x_values[0] = x0

# Apply Euler's Method
for i in range(n_steps):
    x_values[i+1] = x_values[i] + h * f(t_values[i], x_values[i])

# Display the results
print(list(zip(t_values, x_values)))

def improved_euler_method():
    # Improved Euler's Method (Heun's Method)
    x_values_improved = np.zeros(n_steps + 1)
    x_values_improved[0] = x0

    # Apply the Improved Euler Method
    for i in range(n_steps):
        # Predictor step
        x_predict = x_values_improved[i] + h * f(t_values[i], x_values_improved[i])
        
        # Corrector step
        x_values_improved[i+1] = x_values_improved[i] + (h / 2) * (f(t_values[i], x_values_improved[i]) + f(t_values[i] + h, x_predict))

    # Combine results for comparison
    results = list(zip(t_values, x_values, x_values_improved))
    print("Improved Euler's Method Comparison [step/euler/improved]\n", results)

def trigonometric_function_euler():
    # Define the differential equation function
    def dydx(x, y):
        try:
            # Calculate y'(x) using the given expression
            return (2 - np.tan(y)) / (x * (1 / np.cos(y)**2) + (1 / y))
        except ZeroDivisionError:
            # Handle the case when y approaches zero to avoid division by zero
            return 0

    # Initial conditions
    x0 = 0
    y0 = 1
    h = 0.01  # Step size
    n_steps = 10  # Number of steps to reach x = 0.1

    # Arrays to store the values of x and y
    x_values = [x0]
    y_values = [y0]

    # Euler's Method
    for _ in range(n_steps):
        x = x_values[-1]
        y = y_values[-1]
        
        # Compute y'(x) and update y
        y_prime = dydx(x, y)
        y_new = y + h * y_prime
        
        # Update x and store new values
        x_new = x + h
        x_values.append(x_new)
        y_values.append(y_new)

    # Results
    print("Trigonometric Differential Equation Approximate: (step, approximation)\n", list(zip(x_values, y_values)))


improved_euler_method()
trigonometric_function_euler()
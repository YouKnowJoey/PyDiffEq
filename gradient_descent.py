import numpy as np
import matplotlib.pyplot as plt

# Define the loss function and its gradient
def loss_function(theta):
    return (theta - 3) ** 2

def gradient_loss(theta):
    return 2 * (theta - 3)

# Set learning rate and initial parameter value
alpha = 0.1
theta = 0  # Starting point
num_iterations = 100
theta_history = np.zeros(num_iterations)

# Gradient descent loop
for i in range(num_iterations):
    theta = theta - alpha * gradient_loss(theta)  # Update rule
    theta_history[i] = theta  # Store the parameter for visualization

# Visualize the results
plt.plot(range(num_iterations), theta_history, color="blue")
plt.xlabel("Iteration")
plt.ylabel("Parameter Value (theta)")
plt.title("Gradient Descent Optimization")
plt.show()

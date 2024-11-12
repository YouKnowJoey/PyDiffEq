import numpy as np
from scipy.linalg import expm

# Define the matrix A and initial condition x(0)
A = np.array([[1, 2, -1],
              [1, 0, 1],
              [4, -4, 5]])
x0 = np.array([-1, 0, 0])

# Define time at which we want to evaluate x(t)
t = 1  # at t = 1

# Calculate the matrix exponential e^(A * t)
exp_At = expm(A * t)

# Calculate the solution x(t) = e^(At) * x(0)
xt = exp_At @ x0
print(xt)

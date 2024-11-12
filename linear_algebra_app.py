import sympy as sp

# Define the matrix A
A = sp.Matrix([
    [1, 2, -1, 0],
    [3, -1, 2, 1],
    [2, 0, 3, -1],
    [1, -3, 1, 2]
])

# Define the vector b
b = sp.Matrix([5, -1, 4, 2])

# Step 1: Solve the system A*x = b using the inverse method
# x = A^(-1) * b
A_inv = A.inv()  # Inverse of A
x = A_inv * b  # Solution vector

# Step 2: Compute the eigenvalues of the matrix A
eigenvalues = A.eigenvals()

print("Solution to the system of Equations: ", x)
print("Eigenvalues: ", eigenvalues)

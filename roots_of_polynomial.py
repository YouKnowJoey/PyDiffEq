from numpy import roots
import sympy as sp


### Numerical method ###

# Define coefficients of the characteristic polynomial r^3 - 2r^2 - 5r - 6 = 0
coefficients = [1, -2, -5, -6]

# Find the roots of the polynomial
roots_numeric = roots(coefficients)
print(roots_numeric)


### Symbolic Method ###
# Define the variable
r = sp.symbols('r')

# Define the characteristic polynomial
char_eq = r**3 - 2*r**2 - 5*r - 6

# Solve for the roots of the characteristic polynomial
roots_symbolic = sp.solve(char_eq, r)
print(roots_symbolic)

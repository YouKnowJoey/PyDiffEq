import sympy as sp

def general_solution_undetermined_cof():
    # Step 1: Define the symbols and function
    x = sp.symbols('x')
    y = sp.Function('y')(x)

    # Step 2: Define the homogeneous part of the equation (without the forcing function)
    homogeneous_eq = sp.Eq(y.diff(x, 2) + 2*y.diff(x) + 2*y, 0)

    # Solve the homogeneous equation
    homogeneous_sol = sp.dsolve(homogeneous_eq, y)

    # Step 3: Define the non-homogeneous part of the equation (complete equation with forcing function)
    forcing_function = 4*x*sp.exp(-x)*sp.cos(x)
    non_homogeneous_eq = sp.Eq(y.diff(x, 2) + 2*y.diff(x) + 2*y, forcing_function)

    # Step 4: Solve the non-homogeneous equation to find the particular solution
    general_solution = sp.dsolve(non_homogeneous_eq, y)

    # Output the general solution
    print("Homogeneous Solution:",homogeneous_sol)
    print("General Solution:", general_solution)

def general_solution_undetermined_cof_2():

    # Define the variables and function
    x = sp.symbols('x')
    y = sp.Function('y')(x)

    # Define the differential equation
    eq = sp.Eq(y.diff(x, 2) - 4*y.diff(x) + 4*y, x**(-2) * sp.exp(2*x))

    # Solve the homogeneous equation
    homogeneous_solution = sp.dsolve(y.diff(x, 2) - 4*y.diff(x) + 4*y, y)

    # Solve the particular solution using the method of undetermined coefficients
    particular_solution = sp.dsolve(eq, y)

    # Output the general solution
    print("Homogeneous Solution:",homogeneous_solution)
    print("Particular Solution:", particular_solution)

general_solution_undetermined_cof_2()
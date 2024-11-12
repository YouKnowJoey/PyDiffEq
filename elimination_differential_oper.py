import sympy as sp

# Define the variables
t = sp.symbols('t')
x = sp.Function('x')(t)
y = sp.Function('y')(t)
z = sp.Function('z')(t)

# Define the derivatives
Dx = x.diff(t)
Dy = y.diff(t)
Dz = z.diff(t)

# Define the system of equations
eq1 = sp.Eq(Dx, x + 2*y - z)  # x' = x + 2y - z
eq2 = sp.Eq(Dy, x + z)        # y' = x + z
eq3 = sp.Eq(Dz, 4*x - 4*y + 5*z)  # z' = 4x - 4y + 5z

# Rewrite the equations to isolate terms
# Rearranging eq1 to isolate x
x_expr = Dx - 2*y + z

# Substitute x in eq2 and eq3
eq2_sub = eq2.subs(x, x_expr)  # Substitute x in eq2
eq3_sub = eq3.subs(x, x_expr)  # Substitute x in eq3

# Now eq2_sub and eq3_sub will be in terms of y and z
eq2_sub = eq2_sub.simplify()
eq3_sub = eq3_sub.simplify()

# Express eq2_sub and eq3_sub
print(eq2_sub, eq3_sub)

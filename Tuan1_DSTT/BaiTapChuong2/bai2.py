from sympy import symbols, Eq, solve, Matrix

# Problem 1:

x, y = symbols('x y')

eq1 = Eq(x - y, -2)
eq2 = Eq(2*x + 3*y, 6)

sol1 = solve((eq1, eq2), (x, y))
print("Problem 1 solution:", sol1)


# Problem 2:

x, y, z = symbols('x y z')

eq1 = Eq(x - y, 2)
eq2 = Eq(2*x - y + z, 3)
eq3 = Eq(x + y + z, 6)

sol2 = solve((eq1, eq2, eq3), (x, y, z))
print("Problem 2 solution:", sol2)


# Problem 3:

a, b, c = symbols('a b c')

# Thiết lập hệ phương trình:
eq1 = Eq(a*1**2 + b*1 + c, 4)
eq2 = Eq(a*2**2 + b*2 + c, 3)
eq3 = Eq(a*3**2 + b*3 + c, 4)

sol3 = solve((eq1, eq2, eq3), (a, b, c))
print("Problem 3 solution:", sol3)

# Problem 4:

a, b, c = symbols('a b c')

eq1 = Eq(a + b + c, 0)
eq2 = Eq(-2*a + b - 2*c, -3)
eq3 = Eq(-2*a + 2*b + c, 0)

sol4 = solve((eq1, eq2, eq3), (a, b, c))
print("Problem 4 solution:", sol4)

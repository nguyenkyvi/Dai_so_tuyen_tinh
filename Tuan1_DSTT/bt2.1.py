from sympy import Symbol
x = Symbol('x')
f = x + x + x + 2
print(f)
#kq = 3*x + 2


from sympy import Symbol
a = Symbol('Noi')
b = Symbol('Chim')
expression_result = 3 * b + 7 * a
print(expression_result)
#kq = 3*Chim + 7*Noi


from sympy import Symbol
a = Symbol('Noi')
b = Symbol('Chim')
print(a.name)
print(b.name)
#kq = Noi
#kq = Chim


from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
s = x * y + y * x
print(s)
#kq = 2*x*y

p = x * (x + 2 * x)
print(p)
#kq = 3*x**2

p = (x + 2) * (y + 3)
print(p)
#kq = (x + 2)*(y + 3)

p = (x + 2) * (y + 3) + (x + 2) * (x - 3)
print(p)
#kq = (x - 3)*(x + 2) + (x + 2)*(y + 3)

x = Symbol('x')
y = Symbol('y')
p = x * (-x + 2 * x - x)
print(p)
#kq = 0

p = (x + 2) * (y + 3)
print(p.expand())
#kq = x*y + 3*x + 2*y + 6
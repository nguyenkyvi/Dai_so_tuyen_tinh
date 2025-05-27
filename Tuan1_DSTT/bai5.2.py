import sympy as sp
from sympy import Symbol
x1 = Symbol('x1')
x2 = Symbol('x2')
x3 = Symbol('x3')
x4 = Symbol('x4')
from sympy import solve
pt1 = x4+610-450-x1
pt2 = x1+400-x2-640
pt3 = x2+600-x3
pt4 = x3-x4-520
nghiem = sp.solve((pt1, pt2, pt3, pt4))
print(nghiem)
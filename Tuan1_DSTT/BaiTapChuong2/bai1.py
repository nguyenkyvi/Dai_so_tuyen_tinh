import numpy as np

# Hệ phương trình
# x - y = -2
# 2x + 3y = 6
A1 = np.array([[1, -1], [2, 3]])
b1 = np.array([-2, 6])

x1 = np.linalg.solve(A1, b1)
print("Problem 1 solution:", x1)



# Hệ phương trình
# x - y = 2
# 2x - y + z = 3
# x + y + z = 6
A2 = np.array([[1, -1, 0],
               [2, -1, 1],
               [1, 1, 1]])
b2 = np.array([2, 3, 6])

x2 = np.linalg.solve(A2, b2)
print("Problem 2 solution:", x2)



# p(1) = 4, p(2) = 3, p(3) = 4
# Tạo hệ phương trình
A3 = np.array([[1**2, 1, 1],
               [2**2, 2, 1],
               [3**2, 3, 1]])
b3 = np.array([4, 3, 4])

x3 = np.linalg.solve(A3, b3)
print("Problem 3 solution (a, b, c):", x3)



# Tìm a, b, c sao cho:
# (x(x - 3)) / ((x - 1)^2(x + 2)) = a/(x - 1) + b/(x - 1)^2 + c/(x + 2)
# Hệ:
# a + b + c = 0
# -2a + b - 2c = -3
# -2a + 2b + c = 0
A4 = np.array([[1, 1, 1],
               [-2, 1, -2],
               [-2, 2, 1]])
b4 = np.array([0, -3, 0])

x4 = np.linalg.solve(A4, b4)
print("Problem 4 solution (a, b, c):", x4)

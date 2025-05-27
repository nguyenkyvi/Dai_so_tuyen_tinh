import numpy as np

# Bước 1: Tạo ma trận A và vector b
A = np.array([[2, 1],
              [3, 4]])
b = np.array([8, 18])

# Bước 2: Tính ma trận nghịch đảo của A
A_inv = np.linalg.inv(A)

# Bước 3: Tính nghiệm x = A_inv @ b
x = A_inv @ b

print("Nghiệm của hệ phương trình là:", x)

import numpy as np

# Khai báo vec1
vec1 = np.array([1., 3., 5.])
print(f">>> vec1 = {vec1}")


print(f">>> vec1 * 2")
print(vec1 * 2)
# Kết quả: [ 2.  6. 10.]


print(f">>> vec1 * vec1")
print(vec1 * vec1)
# Kết quả: [ 1.  9. 25.]



print(f">>> vec1 / 2")
print(vec1 / 2)
# Kết quả: [0.5 1.5 2.5]


print(f">>> vec1 + vec1")
print(vec1 + vec1)
# Kết quả: [ 2.  6. 10.]

# vec2 = array([2., 4.])
# Lưu ý: Sửa 'array' thành 'np.array'
vec2 = np.array([2., 4.])
print(f">>> vec2 = {vec2}")

# vec1 + vec2
print(f">>> vec1 + vec2")
try:
    print(vec1 + vec2)
except ValueError as e:
    print(f"Lỗi: {e}")

vec3 = np.array([2., 4., 6.])
print(f">>> vec3 = {vec3}")


print(f">>> vec1 + vec3")
print(vec1 + vec3)
# Kết quả: [ 3.  7. 11.]


print(f">>> vec1 / vec3")
print(vec1 / vec3)
# Kết quả: [0.5        0.75       0.83333333]


print(f">>> vec1 * vec3")
print(vec1 * vec3)
# Kết quả: [ 2. 12. 30.]


print(f">>> 2* vec1 + 5* vec3")
print(2 * vec1 + 5 * vec3)
# Kết quả: [11. 26. 35.]
from sympy import Symbol, solve
import numpy as np

x = Symbol('x')
bieuthuc = x + 3 - 5
print(solve(bieuthuc) )
# đáp án 2 

bieuthuc = x**2 + 3 - 5
nghiemx = solve(bieuthuc)
print(nghiemx) 
print(nghiemx[0] ) 
print(nghiemx[1] ) 
# đáp án
# [-sqrt(2), sqrt(2)]
# -sqrt(2)
# sqrt(2)


# Bài tập 2: Giải phương trình bậc 2 


from sympy import solve
x = Symbol('x')
ptb2 = x**2 + 9*x +8
print(solve(ptb2, dict = True))
# đáp án [{x: -8}, {x: -1}]

ptb2 = x**2 + 1*x + 10
nghiemx = solve(ptb2, dict = True)
print(nghiemx)
# đáp án [{x: -1/2 - sqrt(39)*I/2}, {x: -1/2 + sqrt(39)*I/2}]


# Bài tập 3: Giải phương trình 1 biến biểu diễn đại số các biến còn lại 

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
ptb2 = a*x*x + b*x + c
nghiem = solve(ptb2, x, dict=True)
print(nghiem)
# đáp án [{x: (-b - sqrt(-4*a*c + b**2))/(2*a)}, {x: (-b + sqrt(-4*a*c + b**2))/(2*a)}]

# Bài tập 4: Giải hệ phương trình 


from sympy import Symbol, solve
x = Symbol('x')
y = Symbol('y')
pt1 = 2*x+3*y-12
pt2 = 3*x-2*y-5
print(solve((pt1, pt2), dict=True))
# đáp án [{x: 3, y: 2}]

nghiem = solve((pt1, pt2), dict=True)
nghiem = nghiem[0]
print(pt1.subs({x:nghiem[x], y:nghiem[y]}) )
# đáp án [{x: 3, y: 2}]

print(pt2.subs({x:nghiem[x], y:nghiem[y]}))
# đáp án: 0
# 0

# Bài tập 5: Thể hiện ma trận bằng numpy 

M1 = np.array([ [9, 12], [23,30] ])
u = np.array([ 2, 1])
tichM1u = M1.dot(u)
print(tichM1u)
tichuM1 = u.dot(M1)
print(tichuM1) 
print(np.dot(M1, u))
print(np.dot(u, M1))
# đáp án
# [30 76]
# [41 54]
# [30 76]
# [41 54]


# Lệnh 1
mat1 = np.zeros((5, 5))
print("mat1:\n", mat1)

# Lệnh 2
mat2 = np.ones((5, 5))
print("\nmat2:\n", mat2)

# Lệnh 3
mat3 = mat1 + 2 * mat2
print("\nmat3:\n", mat3)

# Lệnh 4
mat4 = mat3

# Lệnh 5
mat3[3][2] = 10
print("\nSau khi gán mat3[3][2] = 10:")
print("mat3:\n", mat3)
print("mat4:\n", mat4)
# -> mat4 cũng thay đổi vì mat4 = mat3 là gán tham chiếu (cùng trỏ 1 vùng nhớ)

# Lệnh 6
mat5 = np.copy(mat3)

# Lệnh 7
mat3[3][2] = 10  # lại gán (trùng giá trị cũ)
print("\nSau khi gán lại mat3[3][2] = 10:")
print("mat3:\n", mat3)
print("mat4:\n", mat4)
print("mat5:\n", mat5)
# -> mat5 KHÔNG đổi vì là bản sao (deep copy)

# Lệnh 8
mat6 = np.empty((4, 5))
print("\nmat6 (giá trị rác - chưa khởi tạo):\n", mat6)

# Lệnh 9
mat7 = np.identity(4)
print("\nmat7 (ma trận đơn vị 4x4):\n", mat7)

# Lệnh 10 (2 lựa chọn)
try:
    mat8 = np.rand((4, 5))  # SAI nếu dùng np.rand (không tồn tại)
except AttributeError:
    mat8 = np.random.random((4, 5))  # đúng
print("\nmat8 (ma trận ngẫu nhiên 4x5):\n", mat8)

# đáp án
# mat1:
#  [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

# mat2:
#  [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

# mat3:
#  [[2. 2. 2. 2. 2.]
#  [2. 2. 2. 2. 2.]
#  [2. 2. 2. 2. 2.]
#  [2. 2. 2. 2. 2.]
#  [2. 2. 2. 2. 2.]]

# Sau khi gán mat3[3][2] = 10:
# mat3:
#  [[ 2.  2.  2.  2.  2.]
#  [ 2.  2.  2.  2.  2.]
#  [ 2.  2.  2.  2.  2.]
#  [ 2.  2. 10.  2.  2.]
#  [ 2.  2.  2.  2.  2.]]
# mat4:
#  [[ 2.  2.  2.  2.  2.]
#  [ 2.  2.  2.  2.  2.]
#  [ 2.  2.  2.  2.  2.]
#  [ 2.  2. 10.  2.  2.]
#  [ 2.  2.  2.  2.  2.]]

# Sau khi gán lại mat3[3][2] = 10:
# mat3:
#  [[ 2.  2.  2.  2.  2.]
#  [ 2.  2.  2.  2.  2.]
#  [ 2.  2.  2.  2.  2.]
#  [ 2.  2. 10.  2.  2.]
#  [ 2.  2.  2.  2.  2.]]
# mat4:
#  [[ 2.  2.  2.  2.  2.]
#  [ 2.  2.  2.  2.  2.]
#  [ 2.  2.  2.  2.  2.]
#  [ 2.  2. 10.  2.  2.]
#  [ 2.  2.  2.  2.  2.]]
# mat5:
#  [[ 2.  2.  2.  2.  2.]
#  [ 2.  2.  2.  2.  2.]
#  [ 2.  2.  2.  2.  2.]
#  [ 2.  2. 10.  2.  2.]
#  [ 2.  2.  2.  2.  2.]]

# mat6 (giá trị rác - chưa khởi tạo):
#  [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

# mat7 (ma trận đơn vị 4x4):
#  [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# mat8 (ma trận ngẫu nhiên 4x5):
#  [[0.76862998 0.83879388 0.69610132 0.99755047 0.82552632]
#  [0.29349816 0.08127746 0.51009487 0.70036076 0.6679553 ]
#  [0.25504163 0.53978393 0.90554189 0.21955955 0.09953919]
#  [0.96111532 0.97758509 0.34200777 0.60960338 0.92539637]]


# Bài tập 6: Tìm chỗ đóng quân:


import numpy as np

# Ma trận nguy cơ
A = np.array([
    [1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1]
])

B = np.array([
    [2, 2, 0, 0, 0],
    [2, 2, 2, 0, 0],
    [1, 1, 2, 0, 0],
    [1, 1, 2, 0, 0],
    [0, 1, 1, 1, 0]
])

C = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 2, 2, 0, 0],
    [2, 2, 2, 2, 2],
    [0, 0, 0, 0, 2]
])

D = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0]
])

E = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
])

# Cấp độ nguy cơ tương ứng
level = np.array([
    [0, 1, 2, 3, 5],  # Chạy rừng
    [0, 2, 3, 4, 5],  # Lũ quét
    [0, 1, 1, 2, 3],  # Sạt lở
    [0, 1, 2, 3, 5],  # Bệnh dịch
    [0, 5, 10, 15, 20]  # Lộ bí mật
])

# Tính tổng điểm nguy cơ cho từng ô
total_risk = (
    level[0][A] +  # cháy rừng
    level[1][B] +  # lũ quét
    level[2][C] +  # sạt lở
    level[3][D] +  # bệnh dịch
    level[4][E]    # lộ bí mật
)

# Điều kiện an toàn: tổng điểm nguy cơ < 5
safe_zone = total_risk < 5

# In kết quả
print("Tổng điểm nguy cơ:\n", total_risk)
print("\nVùng an toàn (True là an toàn):\n", safe_zone)

# đáp án
# Tổng điểm nguy cơ:
#  [[4 3 0 1 0]
#  [3 4 3 1 1]
#  [4 3 5 0 0]
#  [5 5 5 1 1]
#  [6 9 9 7 7]]

# Vùng an toàn (True là an toàn):
#  [[ True  True  True  True  True]
#  [ True  True  True  True  True]
#  [ True  True False  True  True]
#  [False False False  True  True]
#  [False False False False False]]
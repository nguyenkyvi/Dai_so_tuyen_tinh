from sympy import Matrix, pprint

def fibonacci_matrix_power(k):
    # Ma trận Fibonacci cơ bản
    A = Matrix([[1, 1],
                [1, 0]])
    
    # Lũy thừa k
    Ak = A**k
    return Ak

# Ví dụ: tính F_k với k = 5
k = 5
Fk = fibonacci_matrix_power(k)

print(f"Ma trận F^{k}:")
pprint(Fk)

# Các phần tử tương ứng:
F_k_plus_1 = Fk[0, 0]
F_k = Fk[0, 1]
F_k_minus_1 = Fk[1, 1]

print(f"\nFibo_{k+1} =", F_k_plus_1)
print(f"Fibo_{k}   =", F_k)
print(f"Fibo_{k-1} =", F_k_minus_1)

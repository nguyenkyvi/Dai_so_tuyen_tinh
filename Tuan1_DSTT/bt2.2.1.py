from sympy import Symbol, factor 
x = Symbol('x')
y = Symbol('y')
bieuthuc = x**3 - y**3
factored_bieuthuc = factor(bieuthuc)
print(factored_bieuthuc)


from sympy import Symbol, expand 
x = Symbol('x')
y = Symbol('y')
bieuthuc = (x - y) * (x**2 + x * y + y**2)
expanded_bieuthuc = expand(bieuthuc)
print(expanded_bieuthuc)

#2.2.3. Thay thế giá trị
from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x * x - x * y + y * y
giatri = bieuthuc.subs({x: 3, y: 2})
print(bieuthuc)
print(giatri)




# --- Tình huống 1: Xác định theo thứ tự x=3 và y = x ---

giatri_tinhhuong1 = bieuthuc.subs({x: 3, y: x})
print(f"\n--- Tình huống 1: x=3 và y=x ---")
print(f">>> giatri = bieuthuc.subs({{x:3, y:x}})")
print(f">>> giatri")
print(giatri_tinhhuong1) # Expected output is x**2 - 3*x + 9
# Kết quả: x**2 - 3*x + 9

# --- Tình huống 2: Xác định theo thứ tự: x=y và y = 3 ---
giatri_tinhhuong2 = bieuthuc.subs({x: y, y: 3})
print(f"\n--- Tình huống 2: x=y và y=3 ---")
print(f">>> giatri = bieuthuc.subs({{x:y, y:3}})")
print(f">>> giatri")
print(giatri_tinhhuong2)
# Kết quả: 9


giatri_tinhhuong3 = bieuthuc.subs({y: x}).subs({x: 3})
print(f"\n--- Tình huống 3: y=x sau đó x=3 ---")
print(f">>> giatri = bieuthuc.subs({{y:x}}).subs({{x:3}})")
print(f">>> giatri")
print(giatri_tinhhuong3)
# Kết quả: 9



from sympy import Symbol, simplify 
# Define symbols
x = Symbol('x')
y = Symbol('y')


bieuthuc = x*x - x*y + y*y
print(f"bieuthuc: {bieuthuc}")


bieuthuc_moi = bieuthuc.subs({x: 1 - y})
print(f">>> bieuthuc_moi = bieuthuc.subs({{x:1-y}})")
print(f">>> bieuthuc_moi")
print(bieuthuc_moi)


dongian = simplify(bieuthuc_moi)
print(f">>> dongian = simplify(bieuthuc_moi)")
print(f">>> dongian")
print(dongian)



from sympy import Symbol
from sympy import sin, cos, simplify 
x = Symbol('x')
y = Symbol('y')
bt = sin(x) * cos(y) + cos(x) * sin(y)
bt_moi = simplify(bt)
print(bt_moi)
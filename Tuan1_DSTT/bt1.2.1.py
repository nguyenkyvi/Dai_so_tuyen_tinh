danhsach1 = [1., 3.]
danhsach2 = [5., 7.]

# Nối hai danh sách
danhsach = danhsach1 + danhsach2
print(f"danhsach = {danhsach}")
#KQ
#danhsach = [1.0, 3.0, 5.0, 7.0]


# Lặp lại danh sách
danhsach_gapdoi = 2 * danhsach
print(f"danhsach_gapdoi = {danhsach_gapdoi}")
#kqkq
#danhsach_gapdoi = [1.0, 3.0, 5.0, 7.0, 1.0, 3.0, 5.0, 7.0]


# Lặp lại danh sách (tương tự)
print(f"danhsach * 2 = {danhsach * 2}")
#kqkq
#danhsach * 2 = [1.0, 3.0, 5.0, 7.0, 1.0, 3.0, 5.0, 7.0]



# Phép chia danh sách (sẽ gây lỗi)
try:
    print(f"danhsach / 2 = {danhsach / 2}")
except TypeError as e:
    print(f"danhsach / 2 = Lỗi: {e}")
#kq
#danhsach / 2 = Lỗi: unsupported operand type(s)  
    
    
# Các danh sách dữ liệu
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]

# Ghép các danh sách bằng lệnh zip
anh_xa = zip(thu_tu, mon_hoc, diem_so)
print(anh_xa) 
#kqkq
# <zip object at 0xAAAAAAAAAAAA>

tap_hop = set(anh_xa)
print(tap_hop) 
#kqkq
# {(4, 'ToanRR', 8), (1, 'LaptrinhCB', 7), (2, 'ToanCC', 10), (3, 'DSTT', 9)}

anh_xa_lai = zip(thu_tu, mon_hoc, diem_so)
lay_TT, lay_monhoc, lay_diem = zip(*anh_xa_lai)
print(lay_monhoc) 
#kqkq
# ('ToanCC', 'DSTT', 'ToanRR', 'LaptrinhCB')


import itertools
tap_sinh = list(itertools.chain(range(4), range(5,10), range(15,20)))
print(tap_sinh)
#kqkq
# [0, 1, 2, 3, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19]


#Cần tạo 1 bộ 3 thành phần gồm: danh sách từ 0 đến 3; danh sách từ 7 đến 11 và ngược lại một danh sách từ 10. Lệnh Python như sau:
result = list(zip(range(4), range(7, 12), reversed(range(11))))
print(result)
#kqkq
# [(0, 7, 10), (1, 8, 9), (2, 9, 8), (3, 10, 7)]


##########################
#bt1.2.2
mylist = [100, 200, 300]
a,b,c = mylist
print(a, b, c) 
#kq  = 100 200 300

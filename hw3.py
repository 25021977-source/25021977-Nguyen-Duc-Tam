#Bài 9: Nhập vào số nguyên dương a, kiểm tra xem a có phải là số chính phương hay không? Số chính phương là số có căn bậc hai là một số nguyên VD: 1, 4, 9, 16, 25…
import math
a = int(input())
if a > 0:
  if math.isqrt(a) ** 2 == a :
    print(f'{a} la so chinh phuong')
  else :
    print(f'{a} khong la so chinh phuong')
else :
  print('Vui long nhap so nguyen duong')
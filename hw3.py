#Bài 13: Nhập vào số nguyên dương A, tìm n nhỏ nhất sao cho
# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n > A
A = int(input(f'A = '))
if A > 0 :
  sum = 0
  n = 1
  while sum <= A:
    sum += 1 / n
    n += 1
  print(f'n = {n - 1}')
else :
  print("Vui long nhap so nguyen  duong ")

#Bài 3: Nhập vào số nguyên dương a, in ra bảng cửu chương của a 
n = int(input())
if n > 0:
  i = 1
  for i in range(1 , 11):
    print(f'{n} * {i} = {n * i}')
else :
  print("vui long nhap so nguyen duong")
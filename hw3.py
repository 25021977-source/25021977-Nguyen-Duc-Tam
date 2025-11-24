#Bài 18: Nhập vào một số nguyên dương n, kiểm tra xem n có phải là số dạng 3^k hay không
n = int(input())
if n > 0:
  while n % 3 == 0:
    n //= 3
  if n == 1 :
      print("So dang 3^k")
  else :
      print("Khong phai")
else :
  print("Vui long nhap so nguyen duong")
#Bài 17: Nhập vào số nguyên dương n, tính tổng các chữ số của n
n = int(input())
if n > 0 :
  sum = 0
  while n > 0:
    sum += n % 10
    n //= 10
  print(sum)
else :
  print("Vui long nhap so nguyen duong")
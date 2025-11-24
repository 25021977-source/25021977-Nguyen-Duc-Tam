#Bài 20: Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số là số nguyên tố.
n = int(input())
count = 0
if n > 0 :
  while n > 0 :
    a = n % 10
    if a in (2 , 3 , 5 ,7):
      count += 1
    n //= 10
  print(f'{count} so nguyen to')
else :
  print("vui long nhap so nguyen duong")
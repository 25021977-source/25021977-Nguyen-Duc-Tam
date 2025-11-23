#Bài 16: Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ
n = int(input())
if n > 0:
  count = 0
  count_1 = 0
  while n > 0 :
    a = n % 10
    if a % 2 == 0 :
      count += 1 
    else :
      count_1 += 1
    n //= 10
  print(f'{count} so chan')
  print(f'{count_1} so le')
else :
  print("vui long nhap so nguyen duong")
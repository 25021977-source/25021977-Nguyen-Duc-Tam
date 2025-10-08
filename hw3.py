#Bài 7: Nhập vào số nguyên dương a, đếm số ước dương của a 
n = int(input())
if n > 0:
  count = 0
  for i in range(1 , n+1):
    if n  % i == 0 :
      count += 1
  print(count)
else :
  print('Vui long nhap so nguyen duong')
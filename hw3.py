#Bài 6: Nhập vào số nguyên dương a, in ra tất cả các ước dương của a 
n = int(input())
if n > 0:
  for i in range(1 , n+1):
    if n % i == 0 :
      print(i)
else :
  print('Vui long nhap so nguyen duong')
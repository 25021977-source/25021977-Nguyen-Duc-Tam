#Bài 8: Nhập vào số nguyên dương a và b, in toàn bộ ước dương chung của a và b 
a , b = map(int,input().split())
if a > 0 and b > 0:
  for i in range(1 ,a + 1):
    if a % i == 0 and b % i == 0  :
      print(i)
else :
  print("Vui long nhap so nguyen duong")

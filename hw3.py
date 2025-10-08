#Bài 5: Nhập vào số nguyên dương n. Tính S = 1 + 2 + 3 + 4 + … + n 
n = int(input())
s = 0
if n > 0 :
 for i in range(1 , n+1) :
   s +=i
 print(s)
else :
  print("Vui long nhap so nguyen duong")
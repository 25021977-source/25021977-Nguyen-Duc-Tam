#Bài 15: Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số. Làm bằng nhiều cách nhất có thể, ko dùng mảng. 
n = int(input())
if n > 0 :
 count = 0
 while n > 0:
   n //= 10
   count += 1 
 print(count)
else :
  print("Vui long nhap so nguyen duong")

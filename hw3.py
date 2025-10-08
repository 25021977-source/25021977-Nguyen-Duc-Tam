#Bài 12: Nhập số nguyên dương n, Cho S(k) = 1 + 2 + 3 + … + k. Tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n 
n = int(input("n = ")) 
if n > 0:
  sum = 0
  k = 0
  while sum + (k +1)  < n:
    k += 1
    sum += k
  print(f'k = {k}')
else :
  print("Vui long nhap so nguyen duong")
  
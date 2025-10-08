#Bài 10: Nhập vào số nguyên dương a
#kiểm tra xem a có phải là số hoàn hảo hay không. Số hoàn hảo là số có tổng các ước (ước nhỏ hơn nó) bằng chính nó, VD: số 6, 28… 
a = int(input())
if a > 0:
  sum = 0
  for i in range (1 , a ):
    if a % i == 0 :
      sum += i
  if sum == a :
    print(f'{a} la so hoan hao')
  else :
    print(f'{a} khong la so hoan hao')
else :
  print("Vui long nhap so nguyen duong ")
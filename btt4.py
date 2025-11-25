#w4A2
#[PrimeNumber]
#VIết chương trình nhập vào một số tới khi được một số nguyên dương thì thôi.
#Kiểm tra số này có phải là số nguyên tố hay không?
while True :
  n = int(input())
  if n > 0 :
    break
  else :
    print("Vui long nhap so nguyen duong")
#Kiểm tra số này có phải số nguyên tố hay không
if n > 2:
  flag = True
  for i in range(2 , int(n ** 0.5) + 1):
     if n % i == 0:
      flag = False
      break
  if flag :
    print(f'{n} la so nguyen to')
  else :
    print(f'{n} khong la so nguyen to')
else :
  print(f'{n} khong la so nguyen to')



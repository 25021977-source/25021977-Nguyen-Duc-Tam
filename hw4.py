#w4A3
#[Factorial]
#Viết chương trình tính giai thừa của một số nguyên n cho trước (n!=1×2×…×n)với 0 < n < 100
n  = int(input())
if 0 < n < 100 :
 factorial = 1
 i = 1
 while i <= n :
   factorial *= i
   i += 1
 print(f'{n}! = {factorial}')
else : 
 print("Vui long nhap n thoa man (0 < n < 100)")

#w4A7
#"[LargestPrimeFactor]
#Nhập vào số nguyên dương n (n ≥ 2). Hãy in ra ước số nguyên tố lớn nhất của n." 
import math
def nguyen_to(n):
    if n < 2 :
        return False
    for i in range(2 , math.isqrt(n) + 1):
        if n % i == 0:
         return False
    return True
n = int(input())
if n >= 2:
 ans = n
 while ans >= 2:
    if n % ans == 0 and nguyen_to(ans):
     print(ans)
     break
    ans -= 1

   
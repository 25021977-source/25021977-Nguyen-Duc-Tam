#w4A6
#"[SumPrimesInRange]
#Nhập hai số nguyên dương a, b (a ≤ b). 
#Hãy tính tổng các số nguyên tố trong đoạn\[a, b]. Mỗi dòng là một bộ test (a b)."
import math
def nguyen_to(n) :
    if n < 2 :
        return False
    for i in range(2 , math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

a = int(input())
b = int(input())
sum = 0
for j in range(a , b + 1):
    if nguyen_to(j) :
        sum += j

print(sum)
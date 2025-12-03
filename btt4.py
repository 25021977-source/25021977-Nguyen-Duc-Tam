#W4A11 
#[EvenDivisors]
#Viết chương trình đếm số lượng ước số chẵn của số nguyên dương n với n < 10^6
import math
def so_uoc_chan(a) :
    if a >= 10 ** 6 :
        return False
    count = 0
    for i in range(1 , math.isqrt(a)+1) :
        if a % i == 0 :
            j = a // i
            if i % 2 == 0:
                count += 1
            if j != i and j % 2 == 0:
                count += 1 
           
    return count

n = int(input())
print(so_uoc_chan(n))
#W5A3 Viết hàm kiểm tra một số có phải là số nguyên tố hay không? 
import math
def so_nguyen_to(n) :
    if n < 2 :
        return False
    for i in range(2 , math.isqrt(n) + 1 ) :       # isqrt : căn bậc 2
        if n % i == 0 :
            return False
    return True

a = int(input())
if so_nguyen_to(a) :
    print(f"{a} la so nguyen to")
else :
    print(f"{a} khong la so nguyen to")
    
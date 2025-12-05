#W5A6 Viết hàm tính giai thừa. Nhập vào số nguyên n, trả về giai thừa của n (n!) 
def giai_thua( n ) :
    if n < 0 :
        return False 
    s = 1
    for i in range(1 , n + 1 ):
        s *= i
        i += 1
    return s

a = int(input())
print(giai_thua(a))

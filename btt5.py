#W5A4 VIết hàm kiểm tra một số có phải số hoàn hảo hay không, xử lý trên dữ liệu kiểu số nguyên
def so_hoan_hao(a) :
    if a <= 1 :
        return False
    tong = 0
    for i in range(1 , a):
        if a % i == 0:
            tong += i

    return tong == a

n = int(input())
if so_hoan_hao(n) :
    print(f'{n} la so hoan hao')
else :
    print((f'{n} khong la so hoan hao'))

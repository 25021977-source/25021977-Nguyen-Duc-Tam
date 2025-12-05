#W5A9 Viết hàm trả về tổng các chữ số của số nguyên dương n
def tong_duong(n) :
    n = abs(n)       #abs : hàm lấy trị tuyệt đối
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong

n = int(input())
print(tong_duong(n))
        
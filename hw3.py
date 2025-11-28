#Bài 19: Dãy số fibonacci là dãy số được định nghĩa như sau: 1, 1, 2, 3, 5, 8, 13,... với số kế tiếp sẽ bằng tổng hai số trước đó  
#Nhập vào số nguyên dương a, hãy tìm số trong dãy số fibonacci lớn nhất nhưng không vượt quá a
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

a = int(input("Nhap so nguyen duong a: "))

if a <= 0:
    print("Nhap lai")
else:
    n = 0
    while True:
        f = fib(n)
        if f > a:
            print(f"So can tim: {fib(n-1)}")
            break   
        n += 1

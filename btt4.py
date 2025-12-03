#w4A14
#[GCD]
#Cho hai số m và n là hai số nguyên dương nhập từ bàn phím. Viết chương trìnhtìm ước chung lớn nhất của hai số m và n. 
def gcd( a , b ) :
    while b != 0:
        a , b = b , a % b
    return a
m = int(input())
n = int(input())
print(f'{gcd(m,n)}')

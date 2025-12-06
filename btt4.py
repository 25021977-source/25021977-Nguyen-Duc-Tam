#W4A13
#Nhập hai số từ bàn phím và kiểm tra xem chúng có phải là cặp số thân thiết không.
#Nếu có, in ra màn hình "True", ngược lại, in ra "False" 
def than_thiet(a , b):
    count = 0
    count_1 = 0
    for i in range(1 , a) :
        if a % i == 0:
            count += i
    for j in range(1 , b) :
        if b % j == 0 :   
            count_1 += j
    return count == b and count_1 == a
x = int(input())
y = int(input())
print(than_thiet(x , y))
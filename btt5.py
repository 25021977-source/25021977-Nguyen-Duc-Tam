#W5A8
#Cho hai số nguyên x và y, hãy viết hàm trả về khoảng cách Hamming giữa hai số này.
# Khoảng cách Hamming giữa hai số nguyên là số lượng vị trí khác nhau giữa hai dãy bits tương ứng của chúng 
def Hamming(a , a_1 ):
    a = format(a ,'b')        #format(a,'b') : chuyển số nguyên sang nhị phân
    a_1 = format(a_1 ,'b')
    max_len =max(len(a) , len(a_1))
    a = a.rjust(max_len,'0')           #rjust : thêm kí tự vào phần đầu để đạt độ dài mong muốn
    a_1 = a_1.rjust(max_len,'0')

    count = 0
    for i in range(max_len) :
        if a[i] != a_1[i] :
            count += 1
    
    return c
x = int(input())
y = int(input())
print(Hamming(x,y))
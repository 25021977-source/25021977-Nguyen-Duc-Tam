#W5A10 Viết hàm trả về \(true\) nếu hai từ \(a\) và \(b\) là đẳng cấu, ngược lại \(false\).
# Bạn có thể giả sử hai từ đầu vào có cùng độ dài. 
def dang_cau(a , b):
 x = [0] * 256
 x_1 = [0] * 256
 for i in range(len(a)) :
   if x[ord(a[i])] != x_1[ord(b[i])] :
    return False
   x[ord(a[i])] = i + 1
   x_1[ord(b[i])] = i + 1
 return True
x = input()
y = input()
print(dang_cau(x , y))


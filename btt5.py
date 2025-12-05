#Nhập vào 1 dãy số đến khi nhập được 1 số âm hoặc >= 10 thì dừng .
#liệt kê số lần xuất hiện của các số đã nhập tăng dần của số
#không được dùng mảng quá 10 phần tử
count = [0] * 10
while True :
    n = int(input())
    if n < 0 or n >= 10 :
        break
    count[n] += 1
for i in range(10) :
     if count[i] > 0:
       print(i , count[i])



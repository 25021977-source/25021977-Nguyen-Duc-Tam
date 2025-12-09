#W6A2
#Nhập một dòng số nguyên. In ra list tổng tích lũy (phần tử i là tổng từ đầu
#tới vị trí i), giữ nguyên thứ tự
mylist = list(map(int,input().split()))
output_list = []
total = 0
for i in mylist :
    total += i
    output_list.append(total)
print(output_list)

    

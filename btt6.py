#W6A15
#[Lọc dictionary theo giá trị]
#Nhập vào một dictionary có key là chuỗi và value là số nguyên, và một số
#nguyên k ở dòng tiếp theo. Hãy tạo một dictionary mới chỉ chứa các cặp
#key-value từ dictionary ban đầu mà có value lớn hơn k. In ra dictionary mới.
my_list = input().split()
k = int(input())
dic = {}
for item in my_list :
    key , value = item.split(':')
    if int(value) > k :
        dic[key] = int(value)
print(dic)

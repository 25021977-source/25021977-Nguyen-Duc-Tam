#W6A4
#Nhập một dòng gồm các cặp key:value cách nhau bởi dấu cách. 
#Tạo dictionary ánh xạ mỗi key -> list các value theo thứ tự xuất hiện.
#Nếu key lặp lại, thêm vào list của key đó
my_list = input().split()
dic = {}
for item in my_list :
    key , value = item.split(':')
    if key not in dic :
        dic[key] = [value]
    else :
        dic[key].append(value)
print(dic)
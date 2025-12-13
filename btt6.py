#W6A8
#Viết chương trình nhập vào một list các chuỗi, 
#sau đó đếm số lần xuất hiện của từng chuỗi và lưu vào dictionary.
my_list = input().split()
dic = {}
for i in my_list :
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1
print(dic)
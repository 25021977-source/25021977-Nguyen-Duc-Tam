#W6A13
#[Đảo ngược key và value của dictionary]
#Nhập vào một dictionary có value là duy nhất (không trùng nhau). Hãy tạo
#một dictionary mới bằng cách đảo ngược key và value của dictionary ban
#đầu. In ra dictionary mới.
my_list = input().split()
dic = {}
for item in my_list :
    key , value = item.split(':')
    dic[value] = key
print(dic)
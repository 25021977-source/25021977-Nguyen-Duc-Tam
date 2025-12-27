#W7A4
#Viết hàm tìm phần tử có số lần xuất hiện nhiều nhất trong danh sách. Nếu có
#nhiều phần tử cùng số lần, trả về phần tử xuất hiện trước.
def max_idex(arr) :
    dic = {}
    for i in arr :
        if i in dic :
            dic[i] += 1
        else :
            dic[i] = 1
    max_count = 0
    for key , value in dic.items():
        if value > max_count :
            max_count = value 
    output = []
    for key , value in dic.items():
        if max_count == value :
            output.append(key)
    return f"{output[0]} xuat hien nhieu nhat, som nhat,{max_count} lan"
my_list = list(map(int,input().split()))
print(max_idex(my_list))
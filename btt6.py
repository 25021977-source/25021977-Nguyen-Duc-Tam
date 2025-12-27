#W6A23
#VIết hàm xóa đi các số < x có trong mảng
def remove(my_list , x) :
    output_list = []
    for i in my_list :
        if i >= x :
            output_list.append(i)
    return output_list
my_list1 = list(map(int,input().split()))
k = int(input())
print(remove(my_list1 , k))



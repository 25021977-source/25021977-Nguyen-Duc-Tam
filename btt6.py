#W6A22
#Viết hàm đưa vào 1 list số nguyên, tìm và trả về vị trí có giá trị lớn nhất trong list
def max_index(my_list) :
    max_count = my_list[0]
    max_index = 0
    for i in range(len(my_list)) :
        if my_list[i] > max_count :
            max_count = my_list[i] 
            max_index = i
    return max_index

my_list1 = list(map(int,input().split()))
print(max_index(my_list1))



#W6A3
#Nhập một tuple số nguyên (một dòng) và số nguyên k (dòng kế). In ra tuple
#sau khi xoay trái k vị trí. (Giữ nguyên thứ tự tương đối sau xoay; không sắp xếp.)
my_tuple = tuple(map(int,input().split()))
k = int(input())
output_tuple = my_tuple[k:] + my_tuple[:k]
print(output_tuple)

    

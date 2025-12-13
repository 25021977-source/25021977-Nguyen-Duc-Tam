#W6A14
#[Giao của hai danh sách]
#Nhập vào hai dòng, mỗi dòng là một danh sách các số nguyên. Hãy tìm các
#phần tử chung (giao) của hai danh sách này và in ra một list mới chứa các
#phần tử chung đó, không trùng lặp.
my_list1 = list(map(int,input().split()))
my_list2 = list(map(int,input().split()))
output_list = []
for i in my_list1 :
    if i in my_list2 and i not in output_list :
        output_list.append(i)

print(output_list)


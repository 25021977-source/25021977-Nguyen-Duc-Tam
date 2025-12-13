#W6A10
#Viết chương trình nhập vào một danh sách các số nguyên, và số nguyên
#dương k. In ra list gồm các cặp số khác nhau có tổng bằng k. Mỗi cặp là
#một tuple, hai số trong hai tuple có thể giống nhau, thứ tự xuất hiện trong danh
#sách của số thứ nhất nhỏ hơn thứ tự của số thứ 2 tuple trong list được
#sắp xếp theo thứ tự tăng dần của phần tử đầu tiên trong tuple
my_list = list(map(int,input().split()))
k = int(input())
output_list = []
for i in range(len(my_list)):
    for j in range(i + 1 , len(my_list)) :
        if my_list[i] + my_list[j] == k :
            output_list.append((my_list[i] , my_list[j]))

for x in range(len(output_list)) :
    for y in range(len(output_list) - 1 - x) :
        if output_list[y][0] > output_list[y+1][0] :
            output_list[y] , output_list[y+1] = output_list[y+1] , output_list[y]

print(output_list)

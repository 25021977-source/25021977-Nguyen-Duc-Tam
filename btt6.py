#W6A12
#[Tìm phần tử xuất hiện nhiều nhất]
#Nhập vào một list các số nguyên. Hãyt trong số đó. tìm số xuất hiện nhiều lần nhất trong list.
#Nếu có nhiều số cùng có số lần xuất hiện nhiều nhất, hãy in ra số nhỏ nhất
my_list = list(map(int,input().split()))
dic = {}
for i in my_list :
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1

max_count = 0
for key , value in dic.items() :     #for key , value in dic.items() :duyet tung cay value trong dic
    if value > max_count :
        max_count = value

output_list = []
for key , value in dic.items() :
    if value == max_count :
        output_list.append(key)

print(min(output_list))
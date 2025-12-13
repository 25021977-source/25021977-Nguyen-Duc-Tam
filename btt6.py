#W6A11
#[Tách số chẵn và lẻ từ tuple]
#Nhập vào một tuple chứa các số nguyên. Hãy tạo ra hai tuple mới: một chứa
#tất cả các số chẵn và một chứa tất cả các số lẻ từ tuple ban đầu, giữ nguyên
#thứ tự tương đối. In ra hai tuple này trên hai dòng riêng biệt
my_tuple = tuple(map(int,input().split()))
output_1 = []
output_2 = []
my_list = list(my_tuple)
for i in my_list :
    if i % 2 == 0:
        output_1.append(i)
    else :
        output_2.append(i)
print(tuple(output_1))
print(tuple(output_2))
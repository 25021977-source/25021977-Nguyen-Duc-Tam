#W6A1
#Nhập vào một dòng gồm các số nguyên. Hãy loại bỏ phần tử trùng nhưng
#giữ nguyên thứ tự xuất hiện đầu tiên, rồi in ra list kết quả.
#Yêu cầu in ra đúng dạng list Python, ví dụ [1, 2, 3]
mylist = list(map(int,input().split()))
output_list = []
seen_number = set()
for i in mylist :
    if i not in seen_number :
        output_list.append(i)
        seen_number.add(i)

print(output_list)
    
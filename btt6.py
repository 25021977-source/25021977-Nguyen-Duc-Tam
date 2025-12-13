#W6A6
#Viết chương trình nhập vào một danh sách các số nguyên, sau đó in ra tổng các số trong list đó.
my_list = list(map(int,input().split()))
sum = 0
for i in my_list:
    sum += i
print(sum)

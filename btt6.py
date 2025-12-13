#W6A5
#Nhập một list số nguyên, 
#In ra dictionary {'positives': ..., 'negatives': ..., 'zeros': ...} (đếm số >0, <0, =0)
my_list = list(map(int,input().split()))
count = 0
count_1 = 0
count_2 = 0
for i in my_list :
    if i > 0 :
        count += 1
    if i < 0 :
        count_1 += 1
    if i == 0 :
        count_2 += 1
dic = {'positives' : count , 'negative' : count_1, 'zeros' : count_2}
print(dic)

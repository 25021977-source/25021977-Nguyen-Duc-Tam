#W6A28
#Cho một dãy các số nguyên, kiểm tra xem nó là dãy tăng thực sự hay giảm
#thực sự, hay vô danh (không tăng, không giảm)
my_list = list(map(int,input().split()))
tang = True
giam = True
for i in range(len(my_list) - 1):
    if my_list[i] >= my_list[i+1]:
        tang = False
        
    if my_list[i] <= my_list[i+1]:
        giam = False
if tang :
    print('Tang')
elif giam :
    print("Giam")
else :
    print("Vo danh")



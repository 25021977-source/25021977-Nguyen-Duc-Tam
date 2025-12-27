#W6A20
#Viết hàm đưa vào một list số nguyên và một số nguyên dương k. Hãy tìm và
#trả về vị trí của phần tử đầu tiên có giá trị k trong list, nếu không có thì trả về -1

def vi_tri(my_list , k) :   
    for i in range(len(my_list)) :
        if my_list[i] == k :
               return i
    return -1
my_list1 = list(map(int,input().split()))
k1 = int(input())     
print(vi_tri(my_list1 , k1))


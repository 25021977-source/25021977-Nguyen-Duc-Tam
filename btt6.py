#W6A27
#Cho một dãy số nguyên, Tìm và in ra vị trí các số < x (x là giá trị cho trước).
#nếu không có in ra -1
def vi_tri(my_list , x) :
    output_list = []
    for i in range(len(my_list)) :
        if my_list[i] < x :
            output_list.append(i)
    if not output_list :
        return -1
    return output_list
        
    
    
my_list1 = list(map(int,input().split()))
k = int(input())
print(vi_tri(my_list1 , k))



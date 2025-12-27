#W7A2
#Cho danh sách arr và một số nguyên x, đếm xem x xuất hiện bao nhiêu lần
# trong danh sách. def count_occurrences(arr, x) - > int:
def count_occurrences(arr , x) :
    sum = 0
    for i in range(len(arr)):
        if arr[i] == x :
            sum += 1
    return sum
               
my_list = list(map(int,input().split()))
k = int(input())
print(count_occurrences(my_list , k))
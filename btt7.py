#W7A1
#Viết hàm tìm kiếm nhị phân trên một danh sách đã được sắp xếp tăng dần.
#Trả về chỉ số của phần tu hoặc -1 nếu không tìm thấy. mẫu hàm: def
#binary_search(arr, left, right, target):
def binary_search(arr , left , right , target) :
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == target :
            return mid
        elif arr[mid] < target :
            left = mid + 1
        else :
            right = mid -1
    return -1

my_list = list(map(int,input().split()))
my_list.sort()
target1 = int(input())
print(binary_search(my_list , 0 , len(my_list) - 1 , target1 ))

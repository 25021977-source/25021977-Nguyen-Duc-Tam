#W7A3
#Viết hàm thực hiện thuật toán bubble sort, Selection Sort để sắp xếp danh sách
#theo thứ tự tăng dần. Sắp xếp nổi bọt (Bubble Sort); Sắp xếp chọn (Selection Sort)
def bubble_sort(arr) :
    n = len(arr)
    for i in range(n) :
        swapped = False
        for j in range(n - i - 1) :
            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swapped = True
        if not swapped :
            break
    return arr
def selection_sort(arr) :
    n = len(arr)
    for i in range(n):
        min_id = i
        for j in range(i+1 , n):
            if arr[j] < arr[min_id]:
                min_id = j
        arr[i] , arr[min_id] = arr[min_id] , arr[i]
    return arr
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
print(bubble_sort(arr1))
print(selection_sort(arr2))

#W7A5
#Cho danh sách các số nguyên và một số X, đếm tất cả các cặp (a, b) sao cho a + b = X
arr = list(map(int,input().split()))
x = int(input())
so_cap = 0
for i in range(len(arr)) :
    for j in range(i+1 , len(arr)) :
        if arr[i] + arr[j] == x :
            so_cap += 1
print(so_cap)
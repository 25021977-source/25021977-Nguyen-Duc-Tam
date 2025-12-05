#W5A5 Viết hàm đưa vào một list số nguyên và một số nguyên dương k. 
#Hãy tìm và trả về vị trí củaphần tử đầu tiên có giá trị k trong list số nguyên
#nếu không có thì trả về -1 
def list_so_nguyen( n , k ):
    for i in range( len(n) ) :
        if n[i] == k :
            return i
    return -1

b = list(map(int,input().split()))
a = int(input())
print(list_so_nguyen(b , a))
    

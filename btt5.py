# W5A1 Viết hàm truyền vào hai số nguyên a, b. Trả về số lớn hơn trong hai số. def Max_Of_Two(a, b) -> int:
def Max_Of_Two(x , y):
    return int(max(x , y))


a = int(input())
b = int(input())
print(f'{Max_Of_Two(a , b)}')
#Bài 14: Nhập vào một dãy số nguyên, dừng nhập khi người dùng nhập -1.
#Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập. KHÔNG ĐƯỢC dùng mảng 
max_value = None
min_value = None
while True :
  n = int(input())
  if n == -1 :
    break
  else :
    if max_value is None:
      max_value = n
      min_value = n
    else :
      if n > max_value :
        max_value = n
      if n < min_value :
        min_value = n
print(f'So lon nhat la :{max_value}')
print(f'So nho nhat la :{min_value}')
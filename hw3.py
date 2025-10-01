#w3A2
#Hoán đổi hai số không sd biến tạm thời 
#Sử dụng phép toán XOR trên bit để hoán đổi giá trị của hai biến.
x , y = map(int,input().split())
x = x ^ y
y = x ^ y
x = x ^ y
print(x , y)
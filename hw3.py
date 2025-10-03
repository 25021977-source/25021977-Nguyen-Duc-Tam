#w3A3
#Kiểm tra xem một số có phải là lũy thừa của 2 hay không 
#Sử dụng các toán tử bitwise để xác định xem một số có phải là lũy thừa của 2 hay không. 
#Gợi ý: Đối với lũy thừa của 2, n & (n-1) == 0
n = int(input())
if  n > 0 and n & (n -1 ) == 0:
  print("TRUE")
else :
  print("FALSE")
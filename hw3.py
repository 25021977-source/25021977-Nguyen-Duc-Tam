#w3A11
#Phân loại tam giác] 
#Nhập vào 3 số nguyên dương a,b,c là độ dài 3 cạnh của một tam giác. Kiểm tra 3 số đã nhập có tạo thành một tam giác hợp lệ hay không.
#Nếu không in ra "Không phải tam giác". Nếu có, phân loại tam giác đó là "Tam giác đều", "Tam giác cân", hay "Tam giác thường".
a , b , c = map(int,input().split())
if a + b > c and a + c > b and b + c > a :
  if a == b == c :
    print("Tam giac deu")
  elif a == b or a == c or b ==c :
    print("Tam giac can")
  elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2 :
    print("Tam giac vuong")
  else :
    print("Tam giac thuong ")
else  :
  print("Khong phai tam giac")
  
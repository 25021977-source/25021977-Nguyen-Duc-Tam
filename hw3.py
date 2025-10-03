#w3A12
#Kiểm tra năm nhuận] 
#Nhập vào một số nguyên dương n là số năm, kiểm tra xem năm đó có phải là năm nhuận hay không. 
#Năm nhuận là năm chia hết cho 4 nhưng không chia hết cho 100, hoặc chia hết cho 400. Nếu là năm nhuận in ra "Yes", nếu không in ra "No"
n = int(input())
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
  print("Yes")
else : 
  print("No")

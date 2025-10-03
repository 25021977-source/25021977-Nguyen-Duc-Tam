#w3A13
#[Giải phương trình bậc nhất] 
#Nhập vào hai số thực a và b của phương trình ax + b = 0.
#Tìm và in ra nghiệm của phương trình, kết quả làm tròn đến số thập phân thứ 2. In ra "Vô nghiệm" hoặc "Vô số nghiệm" trong trường hợp tương ứng
a , b = map(float,input().split())
if a == b == 0 :
  print("Vo sO nghiem")
elif a == 0 and b != 0 :
  print("Vo nghiem")
else :
  x = -b / a 
  print(f"Phuong trinh co nghiem :x = {x:.2f}")
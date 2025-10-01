#hw2
 #Bài 3 : Tính tam giác: Nhâp vào ba số a,b,c bất kì. Kiểm tra xem nó có thể  là độ dài ba cạnh hay không,
 #nếu  không  thì in  ra màn  hình  ' Khong la ba  canh cua mot tam  giac'.
 #Ngược lại, kiểm tra xem nó là tam giác gì: Đều, Cân, Vuông, hay Tam giác thường. Tính diện tích, chu vi của tam giác và in ra màn hình.
a , b , c = map(float,input().split())
C = a + b + c
p = C  / 2
if a + b > c and a + c > b and b + c > a :
  S = (p * (p - a ) * (p - b) * (p - c )) ** 0.5
  if a == b == c :
    print("Tam giac deu")
  elif a == b or a == c or b == c:
    print("Tam giac can")
  elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Tam giac vuong")
  else:
    print("Tam giac thuong")
  print("Chu vi tam giac la:", C)
  print("Dien tich tam giac la:", S)
else:
  print("Khong la ba canh cua mot tam giac")
#hw2
#Bài 11: Nhập vào tâm và bán kính của một đường tròn. Sau đó nhập vào một điểm A(x, y) bất kì và kiểm tra xem nó có thuộc đường tròn hay không?
xo , yo = map(float,(input("Nhap toa do tam cua duong tron I(xo , yo):")).split())
R = float(input("Nhap ban kinh duong tron la :"))
x , y = map(float,(input("Nhap toa do diem A(x , y)")).split())
if (x - xo)**2 + (y - yo)**2 == R**2 :
  print("Diem A thuoc duong tron tam I")
else :
  print("Diem A khong thuoc duong tron tam I")

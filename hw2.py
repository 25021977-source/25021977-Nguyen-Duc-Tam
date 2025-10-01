#hw2
#Bài 6: Viết chương trình giải phương trình bậc 2 (ax2 + bx + c = 0)
a , b , c = map(float,input().split())
if a == 0 :
# phuong trinh tro thanh b * x + c = 0
  if c == b == 0 :
    print("Phuong trinh co vo so nghiem")
  elif b == 0 and c != b :
    print("Phuong trinh da cho vo nghiem")
  else :
    x = -c / b 
    print("Phuong trinh da cho co nghiem la:",x)
else : 
  delta = b ** 2 - 4 * a * c
  if delta < 0 :
    print("Phuong trinh da cho vo nghiem")
  elif delta == 0 :
    x = -b / (2 * a )
    print("Phuong trinh co nghiem duy nhat la :",x)
  else :
    x1 = (-b + delta ** 0.5 ) / (2 * a )
    x2 = (-b - delta ** 0.5 ) / ( 2 * a )
    print("Phuong trinh co 2 nghiem phan biet la:")
    print("x1 = ",x1)
    print("x2 = ",x2)
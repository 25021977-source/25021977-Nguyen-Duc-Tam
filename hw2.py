#hw2
#Bài 4: Viết chương trình giải phương trìBnh bậc 1 (ax + b = 0)
a , b = map(float,input().split())
if a == b == 0 :
  print("Phuong trinh co vo so nghiem")
elif a == 0 and a != b :
  print("Phuong trinh da cho vo nghiem")
else :
  x = -b / a 
  print("Phuong trinh da cho co nghiem la:",x)
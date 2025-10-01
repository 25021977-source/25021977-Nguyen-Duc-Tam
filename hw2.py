#hw2
#Bài 9: Giải hệ phương trình tuyến tính:
#ax + by = m
#cx + dy = n
a , b , c , d , m , n = map(float,input().split())
if a * d - b * c == 0 : 
  print("He phuong trinh vo nghiem")
else : 
   x = (m * d - b * n ) / (a * d - b * c )
   y = (a * n - c * m ) / (a * d - b * c )
   print("He phuong trinh co nghiem la :")
   print("x = ",x)
   print("y = ",y)
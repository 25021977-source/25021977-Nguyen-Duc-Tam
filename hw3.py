#3A14
#Xếp loại học lực] 
#Nhập vào điểm trung bình của một học sinh và in ra học lực của học sinh đó. 
#Xếp loại học lực theo quy tắc: 
#- >= 8.0: Giỏi
#- >= 6.5: Khá 
#- >= 5.0: Trung bình 
#- < 5.0: Yếu
n = float(input("Nhap diem trung binh:"))
if n >= 8 :
  print("Gioi")
elif n >= 6.5 :
  print("Kha")
elif n >= 5 :
  print("Trung binh")
else :
  print("Yeu")
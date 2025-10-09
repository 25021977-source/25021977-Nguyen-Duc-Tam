#Bài 11: Nhập vào số nguyên a
#Nếu nhập số âm thì yêu cầu nhập lại cho đến khi người dùng nhập đúng số dương.
#Nếu người dùng nhập đúng số dương thì in ra “Bạn nhập đúng quy tắc” và dừng chương trình.
while True :
  a = int(input())
  if a > 0:
    print("Ban nhap dung quy tac")
    break
  else :
    print("Vui long nhap so nguyen duong")
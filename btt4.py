#w4A15
#[ChickenAndDog]
#"Vừa gà vừa chó,
#Bó lại cho tròn,
#Ba mươi sáu con,
#Một trăm chân chẵn"
#Từ bài toán dân gian trên, mở rộng thành chương trình nhận đầu vào là tổng số
#con và tổng số chân của gà và chó. Nếu tìm được số phù hợp, in ra số lượng gà vàsố lượng chó. Ngược lại, in ra "invalid"
tong_con = int(input("Nhap tong so con :"))
tong_chan = int(input("Nhap tong so chan :"))
def so_nguyen(a) :
    if a - int(a) != 0 :
      return False
    return True
x = (tong_chan - 2 * tong_con)/2
y = tong_con - x
if x >= 0 and y >= 0 and so_nguyen(x) and so_nguyen(y) :
   print(f"so luong ga : {int(y)}")
   print(f"so luong cho : {int(x)}")
else  :
   print("invalid")



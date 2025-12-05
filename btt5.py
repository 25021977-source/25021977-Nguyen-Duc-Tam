#W5A7 
#Đầu vào: Hai số thực và phép toán cần thực hiện (trong số các phép toán \(+, -, *, /\)).
#    Đầu ra: Kết quả phép toán làm tròn chữ số thập phân thứ  2
def tinh_toan(a , b , phep_toan):
    if phep_toan == '+' :
        return round(a + b , 2)    #round : làm tròn đến chữ số
    elif phep_toan == '-' :
        return round(a - b , 2)
    elif phep_toan == '*' :
        return round(a * b , 2)
    elif phep_toan == '/' :
        if b == 0:
            return False
        else :
            return round(a / b , 2)
x = float(input("Nhap x ="))
y = float(input("Nhap y ="))
phep_toan = input("Nhap phep toan ")
ket_qua = tinh_toan(x , y , phep_toan)
print(ket_qua)
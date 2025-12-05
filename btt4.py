#W4A12
#[Interest]
#Một người có tài khoản tiết kiệm ở ngân hàng và gửi vào X đồng với lãi suất là 0.7% mỗi tháng.
#Viết chương trình tính số tiền sau N tháng người ấy rút được 
#(cả gốc và lãi, bỏ qua phần lẻ thập phân).  
def tien_gui(X , N) :
    lai_suot = 7 / 1000
    so_tien = X * ( 1 + lai_suot) ** N
    return int(so_tien)
A = int(input("Nhap so tien :"))
n = int(input("Nhap so thang :"))
print(tien_gui(A ,n))
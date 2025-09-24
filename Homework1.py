#hw24
a = float(input("Nhap chieu rong cua hcn la:"))
b = float(input("nhap chieu dai cua hcn la:"))
if(0 < a < b):
  shcn = a * b
  stc = shcn - 157/50 *((a/2)**2)
  print(f'Dien tich trong cay xung quanh la:{stc:.2f}')
else :
  print("Khong thoa man ycbt")

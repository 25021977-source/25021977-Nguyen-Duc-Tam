#Nhập vào họ tên chủ hộ và chỉ số điện kế tháng trước và chỉ số điện kế tháng này,
#tính tiền điện tháng này cho hộ biết:
#- Từ 0 – 50kWh: 1.984 đồng/kWh
#- Bậc 2: Từ 51 – 100 kWh: 2.050 đồng/kWh
#- Bậc 3: Từ 101 – 200 kWh: 2.380 đồng/kWh
#- Bậc 4: Từ 201 – 300 kWh: 2.998 đồng/kWh
#- Bậc 5: Từ 301 – 400 kWh: 3.350 đồng/kWh
#- Bậc 6: Từ 401 trở đi kWh: 3.460 đồng/kWh
ten_chu_ho = input("Ten chu ho ")
chi_so_dien_thang_truoc = int(input("Chi so dien thang truoc"))
chi_so_dien_thang_nay = int(input("chi so dien thang nay"))
so_kw = chi_so_dien_thang_nay - chi_so_dien_thang_truoc
total_money = 0
#loc tu tren xuong
if(so_kw > 400):
  total_money += (so_kw - 400)*3460
  so_kw = 400
if(so_kw > 300):
  total_money += (so_kw - 300)*3350
  so_kw = 300
if(so_kw > 200):
  total_money += (so_kw - 200)*2998
  so_kw = 200
if(so_kw >100):
  total_money += (so_kw - 100)*2380
  so_kw = 100
if(so_kw >50):
  total_money += (so_kw - 50)*2050
  so_kw = 50
total_money += so_kw*1984
total_money = total_money*108/100
print(f'Ho va ten :','so tien phai tra la:',total_money)
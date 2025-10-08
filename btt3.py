#w3A17
#Cấp số nhân 
#Cho 4 số a, b, c, d. Hãy kiểm tra xem 4 số này có thể theo thứ tự tạo thành 1 cấp số nhân với công bội nguyên theo đúng thứ tự a, b, c, d hay không? 
#Gợi ý : Tìm công bội (b / a) nếu b chia hết cho a, sau đó lấy b nhân công bội và so sánh vs c, c nhân công bội và so sánh vs d
a , b , c , d = map(float,input().split())
if a != 0 and b % a == 0:
   x = b // a 
   if c * x == d and b * x == c and a * x == b:
      print(" La cap so nhan")
   else :
      print("Khong phai cap so nhan")
else :
  print("Khong phai cap so nhan")

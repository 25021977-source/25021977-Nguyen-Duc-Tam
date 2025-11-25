#w4A4
#.[CountingDigits]
#Viết chương trình nhập vào một số nguyên n và in ra màn hình số chữ số (trừ dấu)của số đó. Không dùng kiểu dữ liệu string.
n = int(input())
n = abs(n)
if n == 0:
  print(1)
else :
  count = 0
  while n  > 0:
    n //= 10
    count += 1
  print(count)


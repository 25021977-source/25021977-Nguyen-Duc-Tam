#w4A1 
#[SumOfNumBers]
#Viết chương trình Python sử dụng một trong 2 loại vòng lặp for hoặc while để
#tính tống các số nguyên từ 1 đến n. (n <= 1000)
n = int(input())
Sum = 0
for i in range(1 , n+1) :
  Sum += i
print(Sum)
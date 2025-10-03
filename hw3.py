#w3A5
#Viêt chương trình chia một số m cho n, kết quả thu được làm tròn lên
import math
m , n = map(float,input().split())
x = m / n
print(math.ceil(x))
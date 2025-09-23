a ,b , c = map(int,input().split())
if (a + b > c and a + c > b and c + b >a ):
    p_all = a +b +c
    p = p_all/2
    s = mt.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f'Chu Vi la:{p_all:.2f}\n Dien tich la:{s:.2f}')
  
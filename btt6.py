#W6A7
#Viết chương trình nhập vào một tuple, in ra phần tử đầu, phần tử cuối, và tuple đảo ngược
my_tuple = tuple(map(int,input().split()))
x = my_tuple[::-1]            # n[::-1] : duyệt tuple từ cuối về đầu
print(my_tuple[0] , my_tuple[len(my_tuple) - 1] , x)

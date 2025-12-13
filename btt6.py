#W6A9
#Viết chương trình nhập vào hai dictionary. Sau đó gộp lại thành một
#dictionary mới trong đó nếu một key xuất hiện trong cả hai dict, giá trị sẽ
#được cộng lại, nếu chỉ có trong một dict thì giữ nguyên. In ra dictionary mới
#theo thứ tự từ điển tăng dần của key.
#dinh nghia dic
def input_dic() :
    dic = {}
    items = input().split()
    for i in items :
        key , value = i.split(':')  # .split(':') tach chuoi
        dic[key] = int(value)
    
    return dic

dic1 = input_dic()
dic2 = input_dic()
dic = {}
#gop lai
for key , value in dic1.items() :
    if key in dic2 :
        dic[key] = value + dic2[key]
    else :
        dic[key] = value
for key , value in dic2.items() :
    if key not in dic:
        dic[key] = value
#sapxep
dic_sorted = {}
for key in sorted(dic.keys()) :     #sorted() sapxep tang dan
    dic_sorted[key] = dic[key]

print(dic_sorted)
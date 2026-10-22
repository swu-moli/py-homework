u=0
with open("C:\\Users\\123\\Desktop\\test.txt",'r',encoding='UTF-8') as f:
    i=f.read()
    u=i.count('itheima')
    print(u)
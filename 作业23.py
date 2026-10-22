f=open("C:\\Users\\123\\Desktop\\bill.txt",'r',encoding='utf-8')
n=open("C:\\Users\\123\\Desktop\\bill.txt.bak",'w',encoding='utf-8')
for line in f:
    u=line.strip()
    u=u.split(', ')
    if u[4]=='测试':
            continue
    n.write(line)
f.close()
n.close()
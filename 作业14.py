money=int(5000000)
name=input('请输入姓名')
def yue():
    print(f'你的余额还有{money}')
def cun():
    cunkuan=int(input('请你输入存款'))
    global money
    money+=cunkuan
    print(f'你存款{cunkuan},你的余额还有{money}')
def qu():
    qukuan=int(input('请输入取款'))
    global money
    if (qukuan>money):
        print('抱歉你的余额不足')
    else:
        money-=qukuan
        print(f'你取款{qukuan},你的余额还有{money}')
flag=True
while flag:
    print("------------主菜单-------------")
    print(f"{name}，你好，欢迎来到黑马ATN，请选择操作")
    caozuo=input("""查询余额\t【请输入1】
    存款\t【请输入2】
    取款\t【请输入3】1
    推出\t【请输入4】""")
    if caozuo=='1':
        yue()
    elif caozuo=='2':
        cun()
    elif caozuo=='3':
        qu()
    elif caozuo=='4':
        flag=False
print('欢迎下次使用')

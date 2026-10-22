import random
num =random.randint(1,100)
num1=int(input('猜数字'))
while num1!=num:
    if num1>num:
        print('大了')
    else:
        print('小了')
    num1=int(input('再猜数字'))
print('对了')
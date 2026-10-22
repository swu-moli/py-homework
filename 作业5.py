import random
num = random.randint(1,10)
num1=int(input('猜数字'))
if num1!=num:
    print('猜错了')
    if num1>num:
        print('大了')
    else:
        print('小了')
    num2 = int(input('再猜数字'))
    if num2!=num:
            print('猜错了')
            if num2<num:
                print('小了')
            else:
                print('大了')
            num3=int(input("第三次猜"))
            if num3==num:
                    print('对了')
            else:
                    print(f'错了，我猜的是{num}')
    else:
        print('对了')

else:
    print("对")


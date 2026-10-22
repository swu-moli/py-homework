yue=10000
for i in range(1,21):
    if yue==0 :
        break
    import random
    num = random.randint(1, 10)
    if num >= 5:
        print(f"员工{i},绩效{num},领工资1000，账户余额还有{yue}")
        yue-=1000
    else:
        print(f"员工{i},绩效{num},不发工资")
print('工资发完了')

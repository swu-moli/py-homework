def ddj(x):
    print(f'欢迎光临,请出示健康码并测量体温,你的体温是{x}',end='')
    if x>37.5:
        print('你的体温过高需要隔离')
    else:
        print('你的体温正常，可以通行')
ddj(37.3)
ddj(39.3)

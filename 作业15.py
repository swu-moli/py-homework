num_list=[21,25,21,23,22,20]
num_list2=[29,33,30]
num_list.append(31)
num_list.extend(num_list2)
nmu1=num_list.pop(0)
num2=num_list.pop(-1)
num3=num_list.index(31)
print(nmu1,num2,num3)
print(num_list)


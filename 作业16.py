list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
list3=[]
index=0
while index<len(list1):
    num=list1[index]
    if num%2==0:
        list2.append(num)
    index+=1
for num in list1:
    if num%2==0:
        list3.append(num)
print(list3)
print(list2)

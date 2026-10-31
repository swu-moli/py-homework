import numpy as np
"""arr1=np.arange(1,20,2)#1到20内所有奇数，注意不包括stop
print(arr1)"""
"""arr2=np.zeros((3,4))#全0矩阵
print(arr2)"""
"""arr3=np.random.random((5,4))#0到1随机小数
print(arr3)"""
"""A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
x=A*B#对应元素相乘
print(x)
y=np.dot(A,B)#矩阵乘法
print(y)"""
"""arr4=np.arange(1,13)
arr4=arr4.reshape((3,-1))#将一维数组变为矩阵，填-1可以让它自己算
a=arr4[1,:]#提取第二行
print(a)
b=arr4[:,2]#提取第三列
print(b)"""
"""a = np.array([1, 2, 3])
a=a.reshape((-1,1))#将一维数据变为列向量
print(a)"""
"""a = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]]) # 3x3 矩阵
b = np.array([10, 20, 30]) # 1x3 矩阵
print(a+b)#广播机制"""
"""matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
print(np.max(matrix))#不传axis整体聚合，输出标量
print(np.max(matrix,axis=0))#按行压缩，结果长度等于列数
print(np.max(matrix,axis=1))#按列压缩，结果长度等于行数"""
"""np.random.seed(42)
arr = np.random.randint(0, 100, 10)
arr=arr[(arr>50)&(arr%2==0)]#在 NumPy 里，多个条件连接必须用 &（与）、|（或），而且每个条件必须用括号 () 括起来！
print(arr)"""
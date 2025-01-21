import numpy as np

"""mat1 = np.zeros((3,4))
print(mat1)

mat2 = np.ones((3,4))
print(mat2)

mat3 = mat1+2
print(mat3)

mat4 = mat3-1
print(mat4)

mat5=mat4*mat3
print(mat5)

mat6=np.eye(3,3)
print(mat6)

mat7=mat4/2
print(mat7)"""

mat8= np.random.randn(3,5)
print(mat8)

mat9= np.random.rand(3,4)
print(mat9)

mat10 = np.full([3,4],10)
print(mat10)

mat11 = np.arange(5,40, 5)
print(mat11)

mat12 = np.linspace(2,20,5)
print(mat12)

mat13=np.array([[5,8,9],
               [8,6,5],
               [8,6,8]])
print(np.sum(mat13))
print(np.transpose(mat13))
print(np.max(mat13))
print(np.min(mat13))

mat14=np.array([[1,1,1],
               [1,1,1],
               [1,1,1]])
print(np.exp(mat14))
print(np.std(mat13))
print(np.mean(mat13))
print(np.median(mat13))

import numpy as np

matrix1 =np.array([[12,35,45],
           [78,58,65],
           [8,74,65]])
print(matrix1)
print(matrix1.dtype)

matrix2=np.array([[32,5,87],
                  [6,26,9],
                  [78,82,49]])
print(matrix2)
print(matrix2.dtype)
matrix3=np.matmul(matrix1,matrix2)
print(matrix3)

data=np.genfromtxt("profit.csv",delimiter=",",skip_header=1)
print(data.shape)

matrix4=np.array([[22],[55],[88],[99]])
print(matrix4.shape)

mat=np.matmul(data,matrix4)
print(mat)

result=np.concatenate((data,mat),axis=1)
print(result.shape)

np.savetxt("matrixResult.csv",result,"%.2f",header="expen,res,admin,cost")
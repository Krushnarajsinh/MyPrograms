from numpy import *
arr2=array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(arr2)
print("This is:",arr2.ndim,"D Array")
print(arr2.shape)
print(arr2.max())
print(arr2.min())
print(arr2.dtype)
print(arr2.size)
#arr1=arr2.flatten()   #conversion of 2D into 1D
#print(arr1)
#arr3=arr1.reshape(4,3)    #conversion of 1D into 2D
#print(arr3)
#print(arr3.ndim,"D Array")
#arr4=arr1.reshape(6,1,2)   #conversion of 1D into 3D
#print(arr4)
#print(arr4.ndim,"D Array")
#arr5=arr4.flatten()
#print(arr5)             #conversion of 3D into 1D
mat=matrix(arr2)
print(mat)
mat1=matrix('1 2 ;3 4; 5 6;7 8; 9 10; 11 12')
#mat2=mat1+mat
#print("sum of two Matrix is:",mat2)
mat3=mat1*mat
print("Multiplication of two matrix:")
print(mat3)
print()
print(diagonal(mat3))
print(mat3.dtype)


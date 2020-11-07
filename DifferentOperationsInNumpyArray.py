from numpy import *
arr1=array([3,2,4,5,1])
arr2=array([6,7,8,10,9])
#arr1=arr1+5  #Adding 5 to each Elements
#print(arr1)
#arr3=arr1+arr2  #adding two arrays(vectorized operation)
#print(arr3)
#print(concatenate([arr1,arr2]))      concatenate of two arrays
#arr1.sort()     Sorting of array
#arr2.sort()
#print(arr1)
#print(arr2)
#print(cos(arr1))  trigonometry operation
#print(log(arr1))
#print(sin(arr1))
arr=arr1         #Aliasing
print(arr)
print(id(arr1))      #same id of both,both array have same value and addresses are also same, actually they are pointing one array!!
print(id(arr))
arr=arr1.view()   #shallow copy
arr1[0]=1
arr1[2]=3
arr1[3]=4
arr1[4]=5
print(arr)     #both have different addresses but still thay are dependent to each-other
print(arr1)
print(id(arr1))
print(id(arr))
arr=arr1.copy()   #Deep Copy
arr[0]=6
arr[1]=7
arr[2]=8
arr[3]=9
arr[4]=10
print(arr)    #both have different addresses and  thay are independent to each-other
print(arr1)
print(id(arr1))
print(id(arr))
#print(sqrt(arr1))
#print(min(arr))
#print(max(arr))
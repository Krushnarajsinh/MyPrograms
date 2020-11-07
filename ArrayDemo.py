from array import *
arr=array("i",[1,2,3,4,5,6,7])   #here one advantage for array in python that is here you can expand or srink your array according to requirement
#print(arr.typecode)
#print(arr.buffer_info())
#print(len(arr))
#arr.append(3)
#print(arr)
#arr.remove(3)
#print(arr)
for i in arr:
    print(i,end=" ")
    #OR
for i in range(len(arr)):
    print(arr[i],end=" ")
print()
new_arr=array(arr.typecode,(i for i in arr))
print(new_arr)
arr.reverse()
print(arr)
arr.pop(2)
print(arr)
print("Enter the numbers")
a=input().split(" ")  #this is also work as array
a.sort()
print(a)
a=5
if a is 5:
    print("this work")





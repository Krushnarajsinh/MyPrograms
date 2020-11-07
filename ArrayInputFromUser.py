from array import *
arr=array("i",[])
num=int(input("Enter the size of Array:"))
print("Enter the ",num," Integer values in array:")
for i in range(num):
    x=int(input())
    arr.append(x)
print(arr)
val=int(input("Enter Any Value  to find the  index number for that value in array:"))
print("Index number is:",arr.index(val))

#OR

count=0
for i in arr:
    if i==val:
        print("Index number is:",count)
        break
    else:
        count+=1
else:
    print("Your Entered Value is not in Array")


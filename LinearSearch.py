from array import *

def linear_search(list,key):
    for i in range(len(list)):
        if list[i]==key:
            return i
    else:
        return "Not Found"

if __name__=="__main__":
    list=array('i',[])
    num=int(input("Enter the size of an array:"))
    print("Enter the {} Elements in an array:".format(num))
    for i in range(num):
        x=int(input())
        list.append(x)
    key=int(input("Enter an element to search that it is in an array or not:"))
    index=linear_search(list,key)
    if type(index)==int:
        print("Element is found at {} index".format(index))
    else:
        print("Element is {}".format(index))

#this is also done using while loop and insteadof using array we can use list also.



#list=[1,2,3,4,5]
#k=5
#i=0
#while i<len(list):
 #   if list[i]==k:
 #       print("Element at index:",i)
 #   i+=1
#else:
#    print("Not found")


#IN binary searching we must do sorting
count=0
def binary_search(list,key):
    list.sort()
    lower=0
    upper=len(list)-1

    while lower<=upper:
        mid=(lower+upper)//2
        if list[mid]==key:
            globals()["count"]=mid
            return True
        elif list[mid]<key:
            lower=mid+1
        else:
            upper=mid-1
    else:
        return False

list=[]
num=int(input("Enter the size of List:"))
print("Enter the {} Elements in List:".format(num))
for i in range(num):
    x=int(input())
    list.append(x)

key=int(input("Enter an element to search that it is in an array or not:"))

if binary_search(list,key):
    print("Element found at {} index".format(count))
else:
    print("Element is Not found")


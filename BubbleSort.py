from array import *
def bubble(arr):
    print("This is bubble sort")
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp



if __name__=="__main__":
    arr= array('i', [])
    num = int(input("Enter the size of an array:"))
    print("Enter the {} Elements in an array:".format(num))
    for i in range(num):
        x = int(input())
        arr.append(x)
    print(arr)
    bubble(arr)
    print(arr)

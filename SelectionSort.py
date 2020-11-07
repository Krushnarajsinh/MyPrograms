
def selection_sort(list):
    count = 0
    for i in range(len(list)):
        min_pos=i
        for j in range(i+1,len(list)):
            if list[j]<list[min_pos]:
                min_pos=j
        temp=list[min_pos]
        list[min_pos]=list[i]
        list[i]=temp
        count+=1
        print(list)
    print(count)
if __name__=="__main__":
    list=[]
    num=int(input("Enter the size of list:"))
    print("Enter the {} values in A List:".format(num))
    for i in range(num):
        x=int(input())
        list.append(x)
    print("The Sorted List Is Here:")
    selection_sort(list)
    print(list)



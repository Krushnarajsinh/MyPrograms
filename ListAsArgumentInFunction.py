def odd_even(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
list=[]
num=int(input("Howmay values you want to enter in the list:"))
i=1
while i<=num:
    x=int(input("Enter the {}th value in list:".format(i)))
    list.append(x)
    i+=1
print(list)
even,odd=odd_even(list)
print("There are {} even values in list and There are {} odd values in list".format(even,odd))



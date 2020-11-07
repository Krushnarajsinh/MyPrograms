num=int(input("Enter the number of raws:"))
print("This is your pattern:")
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(end=" ")
    for k in range(1, i + 1):                            #for k in range(i,0,-1): ->to print reverse values
        print(k,end="")
    print()
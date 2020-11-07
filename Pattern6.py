num=int(input("Enter the number of raws:"))
print("This is your pattern:")
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
n=int(input("Enter The Number Of rows:").strip())
#TODO:Lenghty Code
for i in range(n):
    c=1
    for j in range(i+1):
        print(c,end="")
        c+=1
    for k in range(i):
        c -= 1
        print(c-1,end="")
    print()

#TODO: Only One Line Code

for i in range(1,n+1):
    print(((10**i)//9)**2)
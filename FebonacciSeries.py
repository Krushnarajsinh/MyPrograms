def feb(num):
    print("Your Febonacci-Series is:")
    a=0
    b=1
    if num<=0:
        print("Enter positive values and the value should be greater than 0")
    elif num==1:
        print(a)
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,num):
            c=a+b
           # if c>99:
            #    break
            a=b
            b=c
            print(c,end=" ")
num=int(input("Enter the positive number here:"))
feb(num)

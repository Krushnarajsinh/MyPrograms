n=int(input("Enter Any positive number Here:"))
i=2
if n>=2:
    while i<n:
        if n%i==0:
            print("Given Number is Not prime")
            break
        i = i + 1
    else:
        print("Given number is prime")

else:
    print("Entered number is not prime")

import sys
print(sys.getrecursionlimit())
print(sys.setrecursionlimit(2000))
def fact(num):
    if num<0:
        return "Negative of factorial is not possible"
    elif num==0:
        return 1
    else:
        x=num
        y=fact(num-1)
        return x*y
num=int(input("Enter the number to find the factorial:"))
result=fact(num)
print("Factorial of {} is:{}".format(num,result),"Using Recursive Method")
#OR
def fect1(num):
    if num<0:
        return "Negative of factorial is not possible"
    elif num==0:
        return 1
    else:
        f=1
        for i in range(1,num+1):
            f=f*i
        return f
res=fect1(num)
print("Factorial of {} is:{}".format(num,res),"Using Iterative Method")
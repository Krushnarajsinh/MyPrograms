#Generally, we have 3 types of error (1)compile time (2)logical error (3)Runtime error
#(1)Compile time error is not an issue because as developer we can solve it at compile time
#this error is syntatical error suppose some spelling mistake forgot some keywords like if i<n <- here we forgot (:)_this is compile time error
#(2)Logical errors are the errors that gives you a wrong output in logical error our program can be run but it gives invalid outpu
#Ex:-2+3 it gives you 4 as an output then it is wrong
#(3)Runtime error is a critical issue because we can not solve it easily
#the moment we get runtime error our software is stopped to worke
#that's not we want
#there for to handle that we must use the concept of Exception Handling

a=int(input("Enter the number A:"))
b=int(input("Enter the number B:"))
try:
    print("Division ofthis both number is:",a/b)  #it's a critical statement their is no guarintee for execution of this statement
    print("Bye")
except Exception as e:
    print("Error is:",e)





#suppose i perform some operation with database and i need to open a connection to connect the detabase
#when our task is over then we must close that connection
#fa=int(input("Enter the number A:"))

a=int(input("Enter the number A:"))
b=int(input("Enter the number B:"))
try:
    print("open connection")
    a=int(input("Enter a number:"))
    print(a)
    print("Division ofthis both number is:", a / b)
    #print("close connection")
except ValueError as e:
    print("Exception:",e)
except ZeroDivisionError as e:
    print("Exception:", e)
except Exception as e:
    print("Exception:", e)
    #print("close connection")
finally:
    print("close connection")
#finally is a block which provide guarintee to exexute the statement that written inside in it
#Even exception occures or not
#hence we need to perform a task that is important to execute even exception occures or not then we can put that statement inside a finally block
#in try block if some error occures then  the statements after that error are not executes


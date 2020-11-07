def fun1():
    print("This is {} function".format(__name__))
def fun2():
    print("This is second {} function".format(__name__))
def fun3(str):
    print("Entered Value is:",str)
def main():
    fun1()
    fun2()
    fun3("Krushnarajsinh")
if __name__=="__main__":
    main()



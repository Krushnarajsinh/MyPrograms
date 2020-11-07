class A:
    def __init__(self,a):
        print("This is A class Constructor","value is:",a)
    def display1(self):
        print("This is display1 method")
class B(A):
    def __init__(self,a):
        super().__init__(5)
        print("This is B class Constructor","value is:",a)
    def display2(self):
        print("This is display2 method")
    def show(self):
        print("Fetching method of A using Super")
        super().display1()

b1=B(10)
b1.show()
b1.display2()
#the moment you create the object of B then compiler first check if there is init() inside B class if it is not then it will check for init() of A and execute it
#But when both A and B class Have Init() method then only init() of B class Is Executed
#therefor to execute init() of A also we need to use one keyword or function which is called as super()
#when you use super() it represent super class A
#by using super() we can access init() as well as all the methods of A
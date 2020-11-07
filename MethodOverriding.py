class A:
    def fun(self):
        print("This is function of class A")

class B(A):
    def fun(self):
        print("This is function of class B")

b=B()
b.fun()
#method overriding means there are more than one function having same name and number of passing parameters or signature but both
#Are in different classes and those classes are in relationship of "Inheritance"
#here fun() of B class overriding the fun() of A class hence fun() of B class is executed first
#if there is no fun() inside B class then fun() of A class is executed but B(A) is condition for that
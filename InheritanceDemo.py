#Single Level Inheritance
class A:
    def display1(self):
        print("This is display1 method")
class B(A):
    def display2(self):
        print("This is display2 method")
b1=B()
a1=A()
a1.display1()
b1.display1()
b1.display2()
#Multilevel Inheritance
class C(B):
    def display3(self):
        print("This is display3 method")

c1=C()
c1.display1()
c1.display2()
c1.display3()

#Multiple Inheritance
class D:
    def display1(self):
        print("This is display4 method")
class E(A,D):
    def display5(self):
        print("This is display5 method")

e1=E()
e1.display1()  #here only display1() for class A is Accepted not D class method ,If here we write E(D,A) then it is acceptalbe for D
e1.display5()
#We can also perform heirarchical inheritance B(A) and C(A)

#MRO means method resolution order this topic belongs to  the mutiple inheritance
#When we have three classes A,B,C and C(A,B)
#Now A and B both having Same methods name then when we create C class object and  try to call those methods then which method is called?
#ofcourse method of A is called because of MRO which says always executes from left to right and here A is passes as left therefor method of A is Executed
#Let's see following example
class A:
    def __init__(self):
        print("This is constuctor of A class")
    def show(self):
        print("This is A's method")

class B:
    def __init__(self):
        print("This is constuctor of B class")

    def show(self):
        print("This is B's method")

class C(A,B):      #try it C(B,A)
    def __init__(self):
        super().__init__()
        print("This is constuctor of C class")
    def display(self):
        print("This is C's method")

c=C()
c.show()
c.display()
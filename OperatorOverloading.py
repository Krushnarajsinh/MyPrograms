#a=5 and b="navin" c=a+b its not possible because they are syntatic suger
#actually when we perform addition operation c=a+b behind the screen following in-built function will run
a=5
b=7
c=int.__add__(a,b)  #it is similar to the c=a+b
print(c)
#same for multiplication,subtraction,division,comparision and for all operation some in-built methods run actually
c=int.__mul__(a,b)
print(c)
#over task is to overload this in-built methods by our userdefined objects of our classes
#following is the example
class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        self.c=self.a+self.b
        print("Summision of integers:",self.c)
    def __add__(self, other):  #self=t1 amd other=t2
        a=self.a+other.a
        b=self.b+other.b
        t3=Test(a,b)
        return  t3
    def __mul__(self, other):
        a=self.a*other.a
        b=self.b*other.b
        t3=Test(a,b)
        return t3
t1=Test(12,10)
t1.sum()
t2=Test(20,30)
t2.sum()
#now i want to perform summision for t1 and t2 means i want to perform sum of two objects
#t3=t1+t2  # Test.__add__(t1,t2)
#print(t3)
#now above line give an error because there is no in-built method to perform the sum of objects which type is Test
#so we need to overload __add__() method
t3=t1+t2
print("Value A:",t3.a,"And value B:",t3.b)
t3=t1*t2
print("Multiplication for A:",t3.a,"And for B:",t3.b)
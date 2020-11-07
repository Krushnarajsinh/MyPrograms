#method overloading is done when more than one method have same name and passing number of arguments are different in each method or
#variables types are differents but in python types are not metters so let's check for number of passing parameters
class Test:
    def sum(self,a,b):
        print("Sum of two integer is:",a+b)
    def sum(self,a,b,c):
        print("Sum of three integer is:",a+b+c)
t=Test()
t.sum(12,20,21)
#t.sum(20,45) The moment when i run this line it gives  an error it said 1 argument 'c'is missing
#THEREFOR WE CAN SAID THAT IN PYTHON THEIR IS NO CONCEPT OF METHOD OVERLOADING
#But indirectly we can do method overloading
class Demo:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("Sum of three integer is:", a + b + c)
        elif a!=None and b!=None:
            print("Sum of two integer is:", a + b)
        elif a!=None:
            print("Only one integer is:",a)
        else:
            print("{} {} {}".format(a,b,c))
d=Demo()
d.sum(1,2,3)
d.sum(1,2)
d.sum(1)
d.sum()
#so by using above logic we can simply do method overloading in python
#Abstact class is a class that object can not be initiated or created and this class should have at least one abstract method
#this class can also have non-abstact methods but we never access it using an object of that class
#In python to use Abstract class and method topic we must need to import one module called 'abc'
#abc=Abstract Base Classes
from abc import ABC,abstractmethod

class Test(ABC):  #it inherites ABC in-built class
    @abstractmethod
    def fun(self):   #in python we can't make any method as empty we must pasify pass keyword , here we only declare fun() method not define it
        pass
    def sum(self,a,b):
        return a+b

class Demo(Test):
    def fun(self):  #If we inherit An abstract class Test then we should need to be override abstract method fun() ,It is a condition

        print("This is an Abstact method of Test class")

#t=Test()
#print(t.sum(12,12))
#t.fun()  #now after IMporting abc if we create and object of Test class then it gives an error
d=Demo()
d.fun()
print(d.sum(12,12))

#Why we need this concept of abstract classes and method If we can do all by using Demo class ?
#Ans:-When we are working on some project with the help of oops concepts then due to pattern requirment we  can use Abstact class concept
#And By using this concept we can apply some restriction on the other class that inherites our Abstract class

#Three Types of Methods (1)Instance Method (2)Class Method (3) Static Method (yes it is different from class method)
#(1) we can use Instance method to mutate(change) or access instance variable
#Accessor(it's Method):-Are thos who only fetch attributes of class
#Mutator(it's Method):-Are thos who can change the value of attributes of class
#(2)we can use Class method to mutate(change) or access class variable
#(3) we can use static methods when we nothing to do with class variables or nothing to do with instance variable we just want to perform some task regarding class

class Demo:
    a=12
    b=10
    def __init__(self):
        self.a=20
        self.b=30
    def show(self): #Instance Method
        print("Sum of instance variables are:",self.a+self.b)
    @classmethod
    def dispaly(cls):  #Class Method
        print("sum of class variables are:",cls.a+cls.b)
    @staticmethod
    def static_display():  #Static Method
        print("This is class Demo:",__name__)
d1=Demo()
print(d1.a) #this is instance variable a
d1.show()
Demo.dispaly()
d1.static_display()
Demo.static_display()

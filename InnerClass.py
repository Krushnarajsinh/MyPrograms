#class inside a antother class is called as inner class
class Student:
    class_name="A"  #Inner class can access class variable but not instance variable of outer class
    def __init__(self,no,name):
        self.no=no
        self.name=name
        self.lap=self.Laptop("HP","i8")
    def show(self):
        print(self.name,"Has Roll Number {}".format(self.no))
        self.lap.show()
    class Laptop:
        def __init__(self,lap_name,cpu_name):
            self.lap_name=lap_name
            self.cpu_name=cpu_name
        def show(self):
            print("{} Laptop  which cpu version is {}".format(self.lap_name,self.cpu_name))
s1=Student(1,"karan")
s2=Student(2,"hitesh")
s1.show()
s2.show()
#We can create object of inner class in two way
#(1) create  inner class object inside the outer class into init() method and (2)create inner class object outside the outer class
#(2)
lap1=Student.Laptop("HP","i5")
lap2=Student.Laptop("Dell","i7")
#this will create two different object for inner class
lap3=s1.lap
lap4=s2.lap
print(id(lap3))
print(id(lap4))
#lap3=s1.lap.show() this can be used when we create inner calss object inside the outer class lap is object created inside init() of outer class
#OR
lap1.show()
lap2.show()
#Two types of variables:-(1)class variable AND (2)Instance variable
class Student:
    class_name="A"  #The variables define outside the __init__() is called as class or static variables
    def __init__(self,roll_no,marks):
        self.roll_no=roll_no      #instance variables always define inside __init__()method
        self.marks=marks          #Here self.roll_no and self.marks are instance variable
    def show(self):
        print(self.roll_no," Roll_Number get {} marks:".format(self.marks),"From class",Student.class_name)

s1=Student(12,88)
s2=Student(1,90)
s1.marks=92   #We can Access instance variable by using object, here we cange the value of mark for s1 student then it will not affects to s2 student's marks it remain same
s1.show()
s2.show()
#class variable can be accessed by class name as well as instance name but mostly we use class name to access class variable
#this calss variable is same for all the instances(s1,s2) that are created for the class(Student)
#If we change the value for class variable then it will affected for all the objects because it is class variable
print(id(s1.class_name))  #here both having same id because this class variable is created only once for all objects
print(id(s2.class_name))
s1.class_name="B"

print(s1.class_name)  #when we change the value using object then it's changes only for that object
print(s2.class_name)
#Here Intially s1->A and s2->A but when we change class_name for s1 then s1->B  but s2 still pointing s2->A
#But if we change the value using class name then it will change for both objects
Student.class_name="C"  #It will not affects s1 class_name value because this s1 is now pointing s1->B
print(Student.class_name)
print(s2.class_name)
print(s1.class_name) #here value for s1=B because new memory is allocated to the s1->class_name


#We have two types of namespace in memory
#class namespace and instrance namespace
#class namespace is an area that store all the class variables
#instance namespace is an area that store all the instance variables
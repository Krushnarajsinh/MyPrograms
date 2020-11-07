#Object is stored in Heap memory of computer
#Every Time when you Execute our program new addresses are allocated to the each objects
class Test:
    def __init__(self):
        self.name="krushnarajsinh"
        self.age=20
    def update_age(self):  #This self can be t1 or t2 but when we call this function by t1 then t1 is our caller object therefor t1 become self
        self.age=30
    def update_name(self):
        self.name="XYZ"
    def compare(self,t2):
        if self.name==t2.name and self.age==t2.age:
            print("both are same")
        else:
            print("both are different")

t1=Test()   #Size of object is decided by the number of variables we have
t2=Test()   #Constructor is responsible to assign those memory for objects
#print(id(t1))  #Every time you got new address when you run
#print(id(t2))   #Every time you got new address when you run
if t1==t2:
    print("This is done")
else:
    print("this is not done")
t1.compare(t2)
print(t1.name)
t2.update_name()
print(t2.name)
print(t1.age)
t2.update_age()
print(t2.age)
t2.compare(t1)
class A:
    def sum(self,a,b):   #Methods Inside Class And Here self represent object
        c=a+b
        print("Sum is:",c)
    def sub(self,a,b):
        c=a-b
        print("Subtraction is:",c)
a1=A()     #A() is also Called as Constructor
a2=A()
a1.sum(12,12)
a1.sub(12,12)
a2.sum(20,20)
a2.sub(12,4)

#OR

A.sum(a1,20,25)
A.sub(a1,20,10)
A.sum(a2,15,20)
A.sub(a2,100,50)
#IN Python Everything is object
#EXAMPLE:
a=5
print(type(a)) #Here we got class int that means "a" is nothing but it is object of class int
print(type(a1)) #Similarly here a1 is object of class A
class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "{} {}".format(self.a,self.b) #now from here we are returning string value
t1=Test(32,56)
#print(t1) #it prints address of that object not a value (32,56)
x=5
print(x)
#here actually behind the screen x.__str__() method run to print value x
#prniting any value means actually we are printing a string print(x)->x is treated as string(assumption by me)
print(t1.__str__()) #when i remove __str__() then it will gives an error and error is non string value is returned
#that means print() method accept string values
print(t1)

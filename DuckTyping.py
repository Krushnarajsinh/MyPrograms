#IN python we consider dynamictypes that means after assigning 5 value to x(x=5) python says yes it is integer variable
#if i assign any string to x then it will become str type variable
#x is just a name actually we are saying the type of 5 is an integer and type of "karan" is str
#then what is DUCKTYPING ?
#if there is a bird who walk like duck ,quack like duck and swim like a duck then that bird should be a duck
#what's that mean !! it is understands below:-
class Laptop:
    def code(self,ide):
        ide.execute()

class Pycharm:
    def execute(self):
        print("this ide mostly use for python Language")
        print("this is also usefull for executing and compiling any python code")
class Eclipse:
    def execute(self):
        print("this ide mostly use for Java Language")
        print("this is also usefull for executing and compiling any python code")


lap=Laptop()
#ide=Pycharm()
ide=Eclipse()
lap.code(ide)

#here does not metter that ide belonges to which class but ide object shold have execute() method
#here behaviour metters only
#we decide the type of x according to which type of value is assigned to it
#if x=5 then it is integer
#and x="karan" then it is str




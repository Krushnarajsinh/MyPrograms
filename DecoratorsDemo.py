def sub(a,b):
    print("Old sub:",a-b)
sub(4,3)
#sub(3,4)  here we get negative result but if we want positive value without changing positions in arguments  we just reamin this(3,4)
#Yes we can do that using following codding
def sub1(a,b):
    if a<b:
        a,b=b,a
    print(a-b)
sub1(3,4)

#But if we have not any permision to change the code of given function or this function is stored in other files and we can just call it
#just similar to the in-built functions like print() etc.we just call these function, we can not made any changes in the code for print()
#For these types of situations we can inroduce the topic of Decorators
#Decorator can be use to add extra features into existing function

def smart_sub(func):    #we can pass function into a function and in python everything is object
    def inner(a,b):   #here we can assume inner as func and HERE  NUMBER OF PERAMETERS SHOULD BE SIMILAR TO THE sub(a,b)
        if a < b:
            a, b = b, a
        return func(a,b)
    return inner
#Here smart_sub(func) return inner function there for we can stored it into another function
sub=smart_sub(sub)  #We can use function just similar to the variables or object this is buity of python
sub(3,4)  #this is new updated sub(a,b)




list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
def merge(l1,l2):
    return l1+l2
list=merge(list1,list2)
print(list)
#Here Operation is just simple we need to just write one line of code which is list1+list2 but here cause we use fuction we are wasting
#- some line of code such as using def and function name these things can be sorted or remove by using lambda
# Here one more Important thing is We can say Lambda as Anonymous Function

f=lambda l1,l2:list1+list2   #here lambda is expression or function
List=f(list1,list2)
print(List)

fun= lambda a,b:a+b
print(fun(2,3))
                  #Here one more Important thing is we can pass any number of variables in lambda but expression shuold be one
                  #FUNCTIONS ARE OBJECTS IN A PYTHON, we can pass function into a function
anonymous=lambda x,y,z:x-y*z
print(anonymous(2,3,4))


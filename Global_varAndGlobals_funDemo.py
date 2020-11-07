x=10 #global variable
print("Id of the global variable:",id(x))
def some():
    x=5   #local variable
    print("In function vslue is:{}".format(x))
    print("Id of local variable:",id(x))
some()
print("Outside a function value is:{}".format(x))

def some2():
    global x
    x=15    #this x is consider as global x which is given to the above first statement
    #x=3     #this x is not consider as local variable this is also taken as global variable

    print("In function vslue is:{}".format(x))
some2()
print("Outside a function value is:{}".format(x))

  #so what we can do if we want local variable with the same name as of x and also we want to update our global variable x=10 inside the function
  #now here we can make use of globsals() function
def some3():
    x=8 #local variable
    print("Id of local variable in some3() function:",id(x))
    print("value of x is:",x)
    a=globals()['x']=30
    print("Value:",a)
    print("Id of a is :",id(a))
some3()
print(x)
print("Id of global x is:",id(x))

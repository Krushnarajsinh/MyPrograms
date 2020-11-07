a=10
b=15

def glob():
    a=12
    b=21
    c=24
    print("Inside the function values are:")
    print("Value of a={},value of b={} and value of c={}".format(a,b,c))
    x=globals()['a']=200
    y=globals()['b']=100
    print("Global values are changed:")
    print("Global values is:",x,y)
print("outside the function values are:")
print("value of a={} and value of b={}:".format(a,b))
glob()
print("value of a={} and value of b={}:".format(a,b))




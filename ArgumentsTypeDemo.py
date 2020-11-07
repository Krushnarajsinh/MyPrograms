def person(name,age):   #Formal Arguments
    print(name)
    print(age+5)
person("Krushnarajsinh",15)  #Actual Arguments
#person(15,"krushnarajsinh")   #Exchange positions
#There are 4 types of Actual Argumnets: (1)Position (2)Keyword (3)Default (4)Variable Length

#(1)Position:-When We pass the values during function calling posion metters above is the example

#(2)Keyword:-During Function calling we can pass values in any order using keywords
person(age=20,name="Rahul")
#person(a=20,b="navin")  keywords name should be match with formal arguments

def add(x,y=12):  #(3)Default:-We can pass default value in formal argument
    c=x+y
    print("sum is:",c)
add(5)
add(2,5)  #When we pass value as actual Argument then the default value is not considered
def add1(x,y,z=1): #always default parameter is last right parameter
    c=x+y+z
    print("Sum  of 3 number is:",c)
add1(2,2)

#(4)variable length :-when we not know howmany parameter need to pass in actual argument then we can use this
def person_details(name,*data):  #here *data is tuple
    print(name)
    print(data)
    for i in data:
        print(i)
person_details("krushnarajsinh","20","Ahemadabad","8511418177")

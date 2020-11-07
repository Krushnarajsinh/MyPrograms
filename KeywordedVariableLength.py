def person(**data):   #Here **data is Keyworded variable length
    print(data)
    #OR
    for i,j in data.items():
        print(i,":",j)
person(name="Krushnarajsinh",age="20",city="ahemadabad",mob_no="8511418177")

# USe Of Dectionary

dict={1:"navin",2:"Raddy",3:"Age is Full"}
print(dict)
for i,j in dict.items():
    print(i,j)
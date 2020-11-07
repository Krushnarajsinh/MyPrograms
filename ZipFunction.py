list1=["sachin's runs","virat's runs","dhoni's runs","Rohit's runs"]
list2=[20000,15000,12000,10000]
zipped=zip(list1,list2)
#print(zipped)  this will prints type or address
zipped=list(zip(list1,list2))
print(zipped)
zipped=dict(zip(list1,list2))
print(zipped)
zipped=set(zip(list1,list2)) #it will print only unique values from two lists and in any order
print(zipped)

for (i,j) in zipped:
    print(i,j)

from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10]

is_even=lambda n:n%2==0
#print(is_even(5)) #False
result=list(filter(is_even,l))   #filter() is in-built function which take two arguments function and sequence and its return sequation which is filtered by some operation
#result=list(map(is_even,l))     Try this also to know the difference between map and filter
print(result)

 #Filter function filtered out some elements in the list and print filtered sequence

double=lambda a:a*2
result1=list(map(double,result))    #map()  perform some operations on list such as addition,mutiplication etc
print(result1)

total=lambda a,b:a+b
result2=reduce(total,l)  #reduce() is imported from functools module and its returns only one value which can be total of all elements of the list or anything
print(result2)
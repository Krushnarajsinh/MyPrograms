list=[1,2,3,4,5,6,7,8,9]

for i in list:
    print(i,end=",")

#OR We can print it onebyone usint iter() function
i=iter(list) #this function return object of Iterator
print("\n{}".format(i.__next__()))  #__next__() or next() this function point to the next value in a list
print(i.__next__())
print(i.__next__())
#OR
print(next(i))
#Here we can see the buity of iterator ,it's preserves previous value of list and then it's point to next value
#Here iterator know the last value of list also

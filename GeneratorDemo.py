#In iterator we need to face some issues like we need to define to functions  iter() and next()
#hence instead of using iterator we can use Generator
#lat's do that
def toptan():
    yield 5  #yield is the keyword that make your method as generator now this is not normal method it is Generator
    #yield also similar to the return keyword but yield returns the value in the form of iterator
    #So, python Give us a Generator that gives iterator
    yield 6
    yield 8
    yield 9
    yield 10
    list=[1,2,3,4,5,6,7]
    yield list
val=toptan()
print(val) #here address of generator is print
#TO print the value we can use next() method
#print(val.__next__())
#print(val.__next__())
#print(val.__next__())
#we can also use for loop and remember that for loop is (inderictly An iterator)
for i in val:
    print(i)

#why we need Generator ?
#Ans:-Suppose you want to fetch some data from your database and  data may  contain 10000 of values
#If you fetch or perform operations on these all value at same time then it will load in your memory
#but we don't want that
#so we can simply fetch one value at a time and perform some operation on it or print that value using Generator
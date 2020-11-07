#we can create our own Iterator object , To creat userdefine Object we must need creat a userdefine a class
#Forthat we need to use  two methods (1) iter() (2) next()
class Demo:
    def __init__(self):
        self.count=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.count<=10:
            val=self.count
            self.count+=1
            return val
        else:
            raise StopIteration  #to stop for loop i need to raise an exception
list=Demo()
print(list.__iter__()) #it returns Address
print(list.__next__())
print(list.__next__())
print(list.__next__(),"\n\n")  #here our own iterator don't know the end value hence we need to specify somme condition in next()

#if in our class we not define iter() method then its gives an error:-
# for i in list:
#TypeError: 'Demo' object is not iterable
for i in list:
    print(i)

#above for loop start from value 4 because till 3 we use above next() methods
#And this is the buity of iterator  its never repeates once it's start untill end value comes

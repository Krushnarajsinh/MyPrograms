def test():
    print("Hello",end=" ")
    print("I am Function")
test()
def sum_mul(x,y):
    c=x+y
    d=x*y
    return c,d
c,d=sum_mul(2,4)
print("sum is:",c,"\nMultiplication is:",d)

def update(x):   #x=a,But x=10   integers and string are imutables  while list is mutable
    x=10
    print(x)
    print(id(x))
a=5
update(a)
print(a)
print(id(a))

def updateforlist(list):
    list[2]=12
    print(list)
    print(id(list))
p=[10,11,13,13,14]
updateforlist(p)
print(p)
print(id(p))


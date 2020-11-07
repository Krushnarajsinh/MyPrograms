class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __lt__(self, other):
        t1=self.a+self.b
        t2=other.a+other.b
        if t1<t2:
            return True
        else:
            return False

t1=Test(12,45)
t2=Test(25,35)
if t1<t2: #Test.__lt__(t1,t2)
    print(" value of t2 is greater")
else:
    print("value of t1 is greater")

#similarly we can use __gt__() for > operator and  for >= we use __ge__()
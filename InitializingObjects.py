class Test:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        c=self.a+self.b
        print("Sum is:{}".format(c))


t1=Test(10,10)
t2=Test(20,20)
t1.sum()
t2.sum()

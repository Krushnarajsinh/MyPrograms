def toptan():
    n=1
    while n<=10:
        sq=n*n
        yield sq  #note:-yield is similar to the return but return keyword terminates your function yield not do that
        n += 1

val=toptan()  #toptan() returns object of generator
for i in val:
    print(i)
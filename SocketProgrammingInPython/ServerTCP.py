from socket import *
ss=socket() #here you can pass 2 arguments (1)network address ipv4 or ipv6 (2)network types TCP or UDP
#by default it is ipv4 and TCP
print("Connection Created...")
ss.bind(("localhost",9999))
ss.listen(3)
print("Waiting for connection...")
count=1
while True:
    c,addr=ss.accept()  #here accept() returns client socket and address
    name=c.recv(1024).decode()   #1024 is buffer memory,decode() converts byte formate
    if count>2:
        c.send(bytes("Connection closed,more than 2 client can not connect",'utf-8'))
        break
    print("Connected with",name,addr)
    c.send(bytes("Welcome in my connection {}".format(name),'utf-8'))
    count+=1
c.close()
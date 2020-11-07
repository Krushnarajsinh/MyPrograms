from socket import *
ss=socket()
print("Connection created...")
ss.bind(("localhost",4444))
print("Waiting for connection...")
c,addr=ss.accept()
print("server is connected with:",addr)
a,b=int(c.recv(1024).decode())   #1024 is the highest value
x=a+b
str(x)
c.send(bytes(x,'utf-8'))
c.close()


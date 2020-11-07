from socket import *
c=socket()
c.connect(("localhost",4444))
print("Connected with server")
a=input("Enter the first number:")
b=input("Enter the second number:")
c.send(bytes(a,b,'utf-8'))
print("Sum is:",c.recv(1024).decode())
c.close()
from socket import *
c=socket()
c.connect(("localhost",9999))
print("you are connected")
name=input("Ener your name:")
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())
c.close()

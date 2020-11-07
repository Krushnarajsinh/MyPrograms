import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Client connected")
name=input("Enter your name:")
c.sendto(name.encode(),("localhost",8888))
print("data is sended...")
print(c.recvfrom(1024))

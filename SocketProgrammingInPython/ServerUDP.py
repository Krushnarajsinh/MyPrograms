import socket
ss=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #here AF_INET means ipv4 address and SOCK_DGRAM means UDP
print("Connection created....")
ss.bind(("localhost",8888))
a,b=ss.recvfrom(1024)
print(a,b)
ss.sendto("Welcome client".encode(),("localhost",8888))


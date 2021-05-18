import socket

host = socket.gethostname()
port = 8090

s = socket.socket()
s.connect((host, port))


print("You are connected to server")
file_name = input("Enter a name for the incoming file :") 
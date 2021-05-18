import socket

host = socket.gethostname()
port = 8090

s = socket.socket()
s.bind((host, port))

print("Server started at port",port)

s.listen(1)

conn, addr = s.accept()

print("Device with address:",addr,"has connected with conn",conn) 
file_name = input("File name :")

try:
	file = open(file_name, 'rb')
	data = conn.send(file)
	file.close()
	print("File sent successfully")
except:
	print("File not found. Please make sure that your file is in this directory")
	input()

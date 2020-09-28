import socket 

ip = socket.gethostbyname('www.google.com')
print(ip)
print(type(ip))
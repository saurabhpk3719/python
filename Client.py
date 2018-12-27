
#Client code

import socket

s=socket.socket()

port=1111

s.connect(('127.0.0.1',port))

print(s.recv(1024))#connect and here 1024 bytes 
                     #data is size of message
                     #from the client
s.close()

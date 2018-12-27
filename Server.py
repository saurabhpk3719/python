
# Server code

import socket

s=socket.socket()#as it is a localhost we need not
                  #to give the parameters.

print("socket created")

port=1111

#bind method

s.bind(('',port))#' ' means localhost
print("bind successfully to portnumber %s"%(port))


#listen method

s.listen(10)#no of request
print("socket is listening")


#accepting request at any time

while True:
   #establish a connection with client
   c,addr=s.accept()
   print("connected to client",addr)

   c.send(b"thank you for connecting")#message to client5
   # here b"__" is a byte code object
   #it is different than the string
   c.close()
   

   

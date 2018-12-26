#socket programming


'program to check the ip address of website using python script with help of'
'socket programming '

'this can be easily done in cmd also just use this command "ping www.websitename.domain"'


import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip= socket.gethostbyname('www.google.com')

print (ip)

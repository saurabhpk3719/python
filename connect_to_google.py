#socket programming


#import modules
import socket, sys


 #create object

try:
   s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   print ("socket created.")
except socket.error as err:
   print("socket failed with error %s"% (err))

port=80

try:
   host_ip=socket.gethostbyname('www.google.com')

except socket.gaierror:
   print("error in resolving the host")
   sys.exit()

s.connect((host_ip,port))# connecting to google

print("connected to google having ip ==%s"%(host_ip))
   

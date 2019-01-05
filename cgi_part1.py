#!C:\Users\shree\AppData\Local\Programs\Python\Python37-32\python.exe
#this is the python executable environment.
#this script going to run on web browser as a html script
#I used wamp serve. it will act as a server.



print ("Content-type:text/html\r\n\r\n")


print ('<html>')
print('<head>')
print('<title>Hello world</title>')
print('</head>')
print('<body>')
print('<h2>Hello world this is saurabh kshirsagar</h2>')
print('</body>')
print('</html>')
#this script have to be stored in cgi-bin directory in wamp folder.
#after saving run file in ur web browser
#command is: 'localhost:port_number/cgi-bin/filename.py'
#before running this script ur wamp apache sercer shuld be started.

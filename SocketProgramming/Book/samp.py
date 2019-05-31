from socket import *

s =socket(AF_INET,SOCK_STREAM)
s.bind(('',9003))
s.listen(5)
i=2
while i:
    c,a  =s.accept()
    print("Received connection name",a)
    c.send("Hello %s\n".encode())
    i-=1
c.close()

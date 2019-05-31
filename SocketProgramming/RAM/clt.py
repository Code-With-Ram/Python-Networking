import sys
import subprocess
import os
import socket


s =  socket.socket()
host=''
port=9002
s.connect((host,port))
msg=11
data=1
while data:
    msg = input()
    s.send(msg.encode())
    print("MSg sent")
    data = s.recv(1024)
    print(data.decode())

s.close()

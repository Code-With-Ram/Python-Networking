import sys
import subprocess
import os
import socket
import sys
import cv2
s = socket.socket()
host = ""
port = 9023

try:
    s.connect((host,port))

except socket.error:    
    s.connect((host,port+1))


path="/home/vineeth/SocketProgramming/Server-Client-Webcam/write.jpg"

while True:


    f=open(path,"wb")
    size=0
    filesize = int(s.recv(1024).decode())
    if filesize !=0:
            print("image size is ",filesize)
            while(True):
                print("Boom..")
            
                chunk = s.recv(1024*1024)
            
                size+=len(chunk)
                print(size)
                f.write(chunk)
                if  size >= filesize:
                    print("Getting off")
                    break
            
            print("Done with writing File")
            f.close()
    else:
            print("File does not exist")
   





    
    img = cv2.imread(path)

    cv2.imshow("MyFace",img)
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
cv2.destroyAllWindows()

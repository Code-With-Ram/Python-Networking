import socket
import sys
import time
import os

#create a socket
def create_socket():
    try:
        global host
        global port
        global s

        host=""
        port=9000
        s= socket.socket()

    except socket.error as msg:
        print("Socket creation error ",str(msg))


def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port ",port)

        s.bind((host,port))
        s.listen(5)
                
        
    except socket.error as msg:
        print("Socket binding error " + str(msg) +"Retrying .....")
        time.sleep(1)
        port+=1
        bind_socket()

def wait():
    print("wait ",end="")
    for i in range(5):
        print(". ",end="")
        time.sleep(0.1)
    print()    

        
def socket_accept():
    conn,address = s.accept()
    print("Connection Established   IP "+address[0] + "Port"+str(address[1]))
    send_command(conn)    

    conn.close()


#send commands to Client
def send_command(conn):
    try:
       os.mkdir("Data")
    except FileExistsError:
       pass 
    client_response = str(conn.recv(1024),"utf-8")
    wait()
    print(client_response,end="")

    
    while True:
        cmd = input()
        if cmd == "g":
            cmd = "getf pic2.jpg"
            #cmd = "getf f.txt"
            
        if cmd == "quit":
             conn.send(str.encode(cmd))
             conn.close()
             s.close()
             sys.exit()

                     
             
        elif cmd[:4] == "getf":
            filename='Data/' + cmd[5:]
            conn.send(str.encode(cmd))
            f=open(filename,"wb")
            size=0
            filesize = int(conn.recv(1024).decode())
            if filesize !=0:
                    print("image size is ",filesize)
                    while(True):
                        print("Boom..")
                    
                        chunk = conn.recv(1024*1024)
                    
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
           
            
            client_response =str(client_response.split()[-2] +" " + client_response.split()[-1]) 
            print(client_response,end="")
            

        elif len(str.encode(cmd)) > 0:
             conn.send(str.encode(cmd))

             client_response = str(conn.recv(1024),"utf-8")
             print(client_response,end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
    
             
            











    

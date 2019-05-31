import cv2
import socket
import os

def server_program():
    # get the hostname
    host = socket.gethostname()
    host=''
    port = 9026  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    print("Waiting for client to send msg...")
    cap = cv2.VideoCapture(0)
    path="/home/vineeth/SocketProgramming/Server-Client-Webcam/write.jpg"

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        ret,frame = cap.read()
        cv2.imshow("Face in server",frame)
        print("haaha")
        i=6
        cv2.imwrite(path,frame)
        try:
            f = open(path,"rb")
            chunk=1
            filesize = str(os.path.getsize(path))
            print("before size over")
            conn.sendall(filesize.encode())
            print("Sending size over")
            while(i):
                chunk = f.read(1024*1024)
                print("sending chunkless")

                conn.sendall(chunk)
                i-=1
                print("sending")
            f.close()
            print("Key")
        except FileNotFoundError:
            print("File does not exist")
            conn.send('0'.encode())
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
    

    conn.close()  # close the connection

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    server_program()

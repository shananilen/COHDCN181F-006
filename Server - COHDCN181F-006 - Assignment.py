from socket import *

host = '127.0.0.1'                                          #define the host ip address
port = 8000                                                 #define the port

s = socket(AF_INET, SOCK_STREAM)                            #Initiating of the TCP socket
s.bind((host,port))                                         #binding the ip address and the port together
s.listen(1)                                                 #listening to the client using the socket
conn, addr = s.accept()
print ("connected by ",addr)                                #shows the conected IP address and the port number
while True:
    data = conn.recv(1024)
    print("Received : ", repr(data.decode('utf-8')))        #Will decode the encoded reply it received from the client
    reply= input("Reply : ")
    conn.sendall(reply.encode('utf-8'))                     #Encoded Reply will be send

conn.close()

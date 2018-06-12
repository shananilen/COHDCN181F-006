from socket import *

host = '127.0.0.1'
port = 8000
s = socket(AF_INET, SOCK_STREAM)
s.connect((host,port))
while True:
    message= input("Message :")
    s.send(message.encode('utf-8'))                         #Encode the message before sending
    print("Awaiting reply ")
    reply=s.recv(1024)
    print("Received : ",repr(reply.decode('utf-8')))        #Decode the message before printing

s.close()

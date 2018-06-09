import socket
import sys
import os

#Create a TCP/IP socket
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

dest_ip = input("Enter Destination IP : ")

#executing Shell command
b = os.system("ping " + dest_ip)

#Using OS module, it allows us to use underlying OS dependant funcationalities

import socket
import sys
import os

#Create a TCP/IP socket
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

dest_ip = input("Enter Destination IP : ")

b = os.system("tracert " + dest_ip)

#same as Ping shell command ** 

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.setsockopt(socket.SOL_SOCKET, socket.REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.IP_HDRINCL)
s.sendto('127.0.0.1'(80,0))

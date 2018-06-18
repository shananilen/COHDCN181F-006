import socket
from ctypes import *
import struct
import binascii
import argparse


class ip_header(Structure):

    _fields_ = [
        ("version", c_ubyte, 4),
        ("ihdl", c_ubyte, 4),
        ("tos", c_ubyte),
        ("len", c_ushort),
        ("id", c_ushort),
        ("offset", c_ushort),
        ("ttl", c_ubyte),
        ("proto", c_ubyte),
        ("checksum", c_ushort),
        ("src", c_uint32),
        ("dst", c_uint32),
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):

        self.version = 4
        self.ihdl = 5
        self.vihdl = self.version * self.ihdl

        self.src_address = socket.inet_ntoa(struct.pack("@I", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("@I", self.dst))

        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        try:
            self.protocol = self.protocol_map[self.proto]
        except:
            self.protocol = str(self.proto)

host = ''
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x800))

while True:

    data = sniffer.recvfrom(65535)[0]
    ip = ip_header(data[14:])

    print(' ... IPv4 Packet ...')
    print 'Version: ', ip.version
    print 'Header Length: ',ip.vihdl
    print 'Protocol: ',ip.protocol
    print 'Source Address: ',ip.src_address
    print 'Destination Address : ',ip.dst_address
    print '\n \n'
   
	


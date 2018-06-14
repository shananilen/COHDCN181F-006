import struct
from ctypes import *

class IPv6(structure):
    _fileds_ = [
        ("version" , c_ubyte, 6),
        ("class", c_ubyte),
        ("lable", c_ubyte , 20),
        ("payload", c_ushort),
        ("nxtheader", c_ubyte),
        ("hoplimit", c_ubyte),
        ("src", c_unit128),
        ("dst", c_unit128)
    ]

def __new__ (self, socket_buffer = None):
    return self.from_buffer_copy(socket_buffer)

def __init__ (self,socket_buffer = None):
    self.src_address = socket.inet_ntoa(struct.pack("@I", self.src))
    self.dest_address = socket.inet_ntoa(struct.pack("@I" ,self.dst))

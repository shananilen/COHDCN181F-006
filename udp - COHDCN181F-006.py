import struct
from ctypes import *

class UDP(structure):
    _fields_ = [
        ("srcport", c_ushort),
        ("destport", c_ushort),
        ("length", c_ushort),
        ("checksm", c_ushort)
    ]

def __new__(self, socket_buffer = None):
    return self.from_buffer_copy(socket_buffer)

def __init__(self,socket_buffer = None):
    self.source_port = socket.inet_ntoa(struct.pack("I@" , self.srcport))
    self.dest_port = socket.inet_ntoa(struct.pack("I@" , self.destport))
    

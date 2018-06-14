import struct
from ctypes import *

class TCP(structure):
    _fields_ = [
        ("scrport", c_ushort),
        ("destport", c_ushort),
        ("sqno", c_unit32),
        ("ackno", c_unit32),
        ("offset", c_ubyte , 4),
        ("res" c_ubyte , 4),
        ("flags", c_ubyte)
        ("window" , c_ushort),
        ("chekcsm" , c_ushort),
        ("pointer", c_ushort)

    ]

def __new__ (self, socket_buffer = None):
        return self.from_buffer_copy(socket_buffer)

def __init__ (self, socket_buffer = None):
        self.source_port = socket.inet_ntoa(struct.pack("I@" , self.scrport))
        self.dest_port = socket.inet_ntoa(struct.pack("I@" , self.destport))

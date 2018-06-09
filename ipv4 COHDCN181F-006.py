import struct
from ctypes import *

class IP(structure):
    _fields_ = {
        ("version" , c_ubyte ,4 ),
        ("ihl" , c_ubyte ,4),
        ("tos" , c_ubyte),
        ("length", c_ushort),
        ("iden", c_ushort), 
        ("offset ", c_ushort),
        ("ttl", c_ubyte),
        ("prot", c_ubyte),
        ("checksum", c_ushort),
        ("src" , c_unit32),
        ("dst", c_unit32)
        }

def __new__ (self,socket_buffer = None ):
         return self.from_buffer_copy(socket_buffer)

def __init__ (self,socket_buffer = None ):
         self.src_address = socket.inet_ntoa(strct.pack("@I" , self.src))
         self.dest_address = socket.inet_ntoa(struct.pack("@I" , self.dst))

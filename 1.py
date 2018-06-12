from ctypes import *
import socket
host = '127.0.0.1'
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x800))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(host,80)
data = s.resvfrom(65565)[0]


class IP(structure):
    _field_ = {

        ("version", c_ubyte, 4),
        ("iheaderl", c_ubyte,4),
        ("tos", c_ubyte),
        ("len", c_ushort),
        ("id", c_ushort),
        ("off", c_ushort),
        ("ttl", c_ubyte, 4),
        ("prot", c_ubyte),
        ("chk", c_short),
        ("src", c_unit32),
        ("dst", c_unit32)

        }

def __new__ (self, socket_buffer = None):
    return self.from_buffer_copy(socket_buffer)

def __init__(self, socket_buffer = None):
    self.src_address = socket.inet_ntoa(struct.pack("@I", self.src))
    self.dst_address = socket.inet_ntoa(struct.pack("@I", self.dst))
    print(self.src_address)

from mbUtils import writeMultRegs, sockSend, readRegs
from time import sleep
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("192.168.0.2", 502))
    role = b'\x00\x00'
    roleNameAddr = 7386
    msg = writeMultRegs(1, roleNameAddr, role)
    sockSend(msg, s)


finally:
    print("end")
    s.close()
from mbUtils import writeMultRegs, sockSend, readRegs,readCoils, readDiscInput
from time import sleep
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("192.168.0.2", 502))
    Addr = 527
    msg = readRegs(3, Addr, 6)
    sockSend(msg, s)


finally:
    print("end")
    s.close()
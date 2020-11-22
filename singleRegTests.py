from mbUtils import writeMultRegs, sockSend, writeSingleReg
from time import sleep
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("192.168.0.2", 502))

    data = 0
    addr = 7386
    msg = writeSingleReg(1, addr, data)
    sockSend(msg, s)


finally:
    print("end")
    s.close()
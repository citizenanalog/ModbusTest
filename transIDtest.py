from mbUtils import readRegs, sockSend
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
fail = 0
try:
    s.connect(("192.168.0.2", 502))
    for x in range(1, 10):
        msg = readRegs(x, x, 1)
        respMsg = sockSend(msg, s)
        if respMsg[7] == 0x83 or respMsg == '':
            fail = 1
            print(respMsg)
finally:
    s.close()
    if fail == 1:
        print("Error")

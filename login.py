from mbUtils import writeMultRegs, sockSend, readRegs
from time import sleep
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("192.168.0.2", 502))
    #role = b"operator\x00"
    role = b"admin\x00\x00\x00\x00"
    roleNameAddr = 7473
    msg = writeMultRegs(1, roleNameAddr, role)
    sockSend(msg, s)

    #passW = b"O!h11111"
    passW = b"Coriolis5700"
    tempPassAddr = 7466
    msg = writeMultRegs(2, tempPassAddr, passW)
    sockSend(msg, s)

    sleep(0.250)
    loginStatusAddr = 7445
    sessionStatusAddr = 7444
    msg = readRegs(3, loginStatusAddr, 1)
    respMsg = sockSend(msg, s)
    if respMsg[7] != 0x83:
        if respMsg[10] == 0x00:
            print("WAITING")
        if respMsg[10] == 0x01:
            print("LOCKED_OUT")
        if respMsg[10] == 0x02:
            print("INVALID_CREDS")
        if respMsg[10] == 0x03:
            print("AUTHENTICATED")
        if respMsg[10] == 0x04:
            print("NO_SESSIONS_AVAIL")

    msg = readRegs(3, sessionStatusAddr, 1)
    respMsg = sockSend(msg, s)
    if respMsg[7] != 0x83:
        if respMsg[10] == 0x00:
            print("OPEN")
        if respMsg[10] == 0x01:
            print("ADMIN_LOGGED_IN")
        if respMsg[10] == 0x02:
            print("OPER_LOGGED_IN")
        if respMsg[10] == 0x03:
            print("GUEST_LOGGED_IN")

finally:
    print("end")
    s.close()

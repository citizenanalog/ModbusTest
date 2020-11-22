from mbUtils import writeMultRegs, sockSend, readRegs, readCoils
import socket
import math
from struct import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mbReglist = ["0"]
mbCoilList = ["0"]
numScanRegs = 40
numScanCoils = 700
try:
    s.connect(("192.168.0.2", 502))

    for x in range(1, numScanRegs):
        msg = readRegs(x, x, 1)
        respMsg = sockSend(msg, s)
        if respMsg[7] != 0x83:
            mbReglist.append(x)

    for x in range(1, numScanCoils):
        msg = readCoils(x, x, 1)
        respMsg = sockSend(msg, s)
        if respMsg[7] != 0x81:
            mbCoilList.append(x)

    print("Registers=")
    print(*mbReglist, sep=", ")
    print("Coils=")
    print(*mbCoilList, sep=", ")


finally:
    print("end")
    s.close()

'''
scrapyard
print(respMsg[7])

mblist.append(respMsg[7])

packFormat = '>HHHBBHHB' + str(byteCount) + 's'
msg = pack(packFormat, transID, protoID, length, unitID, functCode, addr, numRegs, byteCount, dataValues)

""" 
    for x in range(1, 1000):
        msg = readRegs(x, x, 1)
        respMsg = sockSend(msg, s)
        if respMsg[7] != 0x83:
            print(respMsg[7])
"""
'''

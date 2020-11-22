import socket
import math
from struct import *


def createmsg(transID, protoID, length, unitID, functCode, addr, numRegs, byteCount, dataValues):
    if transID > 65535 or protoID > 65535 or length > 65535 or unitID > 255 or functCode > 255 or addr > 65535 or numRegs > 65535:
        msg = ''
    else:
        packFormat = '>HHHBBHHB' + str(byteCount) + 's'
        msg = pack(packFormat, transID, protoID, length, unitID, functCode, addr, numRegs, byteCount, dataValues)

    return msg


def readRegs(transID, addr, numRegs):
    protoID = 0
    unitID = 111
    functCode = 3
    addr = addr - 1
    length = 6
    if transID > 65535 or length > 65535 or addr > 65535 or numRegs > 65535:
        msg = ''
    else:
        msg = pack('>HHHBBHH', transID, protoID, length, unitID, functCode, addr, numRegs)

    return msg

def readCoils(transID, addr, numRegs):
    protoID = 0
    unitID = 111
    functCode = 1
    addr = addr - 1
    length = 6
    if transID > 65535 or length > 65535 or addr > 65535 or numRegs > 65535:
        msg = ''
    else:
        msg = pack('>HHHBBHH', transID, protoID, length, unitID, functCode, addr, numRegs)

    return msg

def readDiscInput(transID, addr, numRegs):
    protoID = 0
    unitID = 111
    functCode = 2
    addr = addr - 1
    length = 6
    if transID > 65535 or length > 65535 or addr > 65535 or numRegs > 65535:
        msg = ''
    else:
        msg = pack('>HHHBBHH', transID, protoID, length, unitID, functCode, addr, numRegs)

    return msg

def writeMultRegs(transID, addr, dataValues):
    protoID = 0
    unitID = 111
    functCode = 16
    addr = addr - 1
    numRegs = math.ceil(len(dataValues) / 2)
    byteCount = numRegs * 2
    length = 7 + byteCount
    format = '>HHHBBHHB' + str(byteCount) + 's'

    msg = pack(format, transID, protoID, length, unitID, functCode, addr, numRegs, byteCount, dataValues)
    return msg

def writeSingleReg(transID, addr, dataValue):
    protoID = 0
    unitID = 111
    functCode = 6
    addr = addr - 1
    length = 6
    msg = pack('>HHHBBHH', transID, protoID, length, unitID, functCode, addr, dataValue)
    return msg

def sockSend(msg, s):
    if msg != '':
        print("msg = ")
        print(' '.join(format(y, '02x') for y in msg))
        s.sendall(msg)
        s.settimeout(5.0)
        resp = s.recv(4096);
        # print(resp.hex())
        print("resp = ")
        print(' '.join(format(y, '02x') for y in resp))
    else:
        resp = ''
        print("createMBmsg(): input argument error")
    return resp

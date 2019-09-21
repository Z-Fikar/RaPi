import bluetooth as bt

from settings import *

sock = bt.BluetoothSocket(bt.L2CAP)

bd_addr = SERVER_MAC_ADDRESS
port = 0x1001

sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()

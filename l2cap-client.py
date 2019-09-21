import bluetooth as bt

from settings import *

bd_addr = SERVER_MAC_ADDRESS
port = 1

sock = bt.BluetoothSocket(bt.RFCOMM)
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()

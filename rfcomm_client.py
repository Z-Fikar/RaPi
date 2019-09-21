import bluetooth as bt

bd_addr = "DC:A6:32:12:ED:DB"
port = 1

sock = bt.BluetoothSocket(bt.RFCOMM)
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()

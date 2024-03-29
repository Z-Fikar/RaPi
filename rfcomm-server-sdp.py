# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $

import bluetooth as bt
from settings import *

server_sock = bt.BluetoothSocket(bt.RFCOMM)
server_sock.bind((SERVER_MAC_ADDRESS, bt.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = UUID

bt.advertise_service(server_sock, "SampleServer",
                     service_id=uuid,
                     service_classes=[uuid, bt.SERIAL_PORT_CLASS],
                     profiles=[bt.SERIAL_PORT_PROFILE],
                     #   protocols = [ OBEX_UUID ]
                     )

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0:
            break
        print("received [%s]" % data)
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")

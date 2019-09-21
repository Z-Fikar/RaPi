# file: l2capclient.py
# desc: Demo L2CAP server for pybluez.
# $Id: l2capserver.py 524 2007-08-15 04:04:52Z albert $

import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

port = 0x1001

server_sock.l2cap_bind(("", port))
server_sock.l2cap_listen()

#uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ef"
# bluetooth.advertise_service( server_sock, "SampleServerL2CAP",
#                   service_id = uuid,
#                   service_classes = [ uuid ]
#                    )

client_sock, address = server_sock.l2cap_accept()
print("Accepted connection from ", address)

data = client_sock.l2cap_recv(1024)
print("Data received: ", str(data))

while data:
    client_sock.l2cap_send('Echo => ' + str(data))
    data = client_sock.l2cap_recv(1024)
    print("Data received:", str(data))

client_sock.l2cap_close()
server_sock.l2cap_close()

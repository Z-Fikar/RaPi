import bluetooth as bt

server_sock = bt.BluetoothSocket(bt.RFCOMM)

port = 1
server_sock.bind(("DC:A6:32:12:ED:DB", port))
server_sock.listen(1)

print("Waiting connection...")
client_sock, address = server_sock.accept()
print("Accepted connection from {}({})".format(
    address, bt.lookup_name(address)))

data = client_sock.recv(1024)
print("received [{}]".format(data))

client_sock.close()
server_sock.close()

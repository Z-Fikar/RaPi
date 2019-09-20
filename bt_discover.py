import bluetooth as bt

nearby_devices = bt.discover_devices()

for address in nearby_devices:
    print("{}: {}".format(address, bt.lookup_name(address)))

import subprocess as sp

sp.call(['sudo', 'hciconfig', 'hci0', 'piscan'])
print("BLUETOOTH: ON")

# If you want to make rapi undiscoverable
#sp.call(['sudo', 'hciconfig', 'hci0', 'noscan'])
#print("BLUETOOTH: OFF")

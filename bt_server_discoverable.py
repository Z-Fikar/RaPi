import subprocess as sp

sp.call(['sudo', 'hciconfig', 'hci0', 'piscan'])

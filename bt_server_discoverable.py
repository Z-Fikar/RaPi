import subprocess as sp
import time as t

sp.call(['sudo', 'hciconfig', 'hci0', 'piscan'])
t.sleep(10)
sp.call(['sudo', 'hciconfig', 'hci0', 'noscan'])

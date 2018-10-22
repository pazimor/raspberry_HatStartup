# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/humidity-2018-03-11-20-48-10.py"

from sense_hat import SenseHat
import socket
import fcntl
import struct
import time
import os

def getIP(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try :
        ret = socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,
            struct.pack('256s',ifname[:15]))[20:24])
        return ret
    except :
        return ""
hat = SenseHat()
Rd = [255, 0, 0]
startedIP = getIP('eth0')

cmd = "netstat -tn | grep :22 | wc -l"

while True:
	os.system("bash -c '%s' > tmp.txt" % cmd)
	answer = open("tmp.txt", "r")

	if int(answer.read(1)) == 0:
		try:
			hat.show_message(getIP('eth0'), 0.1, Rd)
			hat.clear()
		except:
			hat.show_message(startedIP, 0.1, Rd)
			hat.clear()
	else:
		sleep(10)


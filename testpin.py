#!/usr/bin/env python
import os
import time
import sys

chan = sys.argv[1]
pin = sys.argv[2]
if chan == "A":
	pos = pin
elif chan == "B":
	pos = str(int(pin)+32)
elif chan == "C":
	pos = str(int(pin)+64)
com1 = "echo "+pos+" >/sys/class/gpio/export"
com2 = "echo out > /sys/class/gpio/pio"+chan+pin+"/direction"
com3  = "echo 1 > /sys/class/gpio/pio"+chan+pin+"/value"
com4  = "echo 0 > /sys/class/gpio/pio"+chan+pin+"/value"
print com1
os.system(com1)
print com2
os.system(com2)
print com3
os.system(com3)
time.sleep(1)
print com4
os.system(com4)

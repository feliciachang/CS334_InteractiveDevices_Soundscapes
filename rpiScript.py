from time import sleep
from pythonosc.dispatcher import Dispatcher
import serial
import re
ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 9600)

dispatcher = Dispatcher()

sleep(1)
while True:
	input = ser.readline()
	print(input)
	

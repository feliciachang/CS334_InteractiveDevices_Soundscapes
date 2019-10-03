from time import sleep
import random
import serial # sudo pip install pyserial
import re

ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 9600)

def main():
    while True:
        print("starting")
        serialData = ser.readline()
        print(serialData)

if __name__ == "__main__":
	main()

from time import sleep
import random
import serial # sudo pip install pyserial
import re
import gpiozero as gp

ser = serial.Serial('/dev/ttyAMA0', 9600)

def main():
    while True:
        print("starting")
        serialData = ser.readline()
        print(serialData)

if __name__ == "__main__":
	main()

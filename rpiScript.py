#!/usr/bin/env python

#counter thingy for joystick that increments it downward

from time import sleep
import OSC # sudo pip install pyOSC
import serial # sudo pip install pyserial
import re
import gpiozero as gp

ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 9600)

enable_osc = True

# tree, car, wave, leaf
# wildcard, iterate
# amp, shift, wildX, wildY

#resting vals of param control joysticks
#2675 amp stick
#2915 shift stick

prevStates = [0, 0, 0, 0, \
			 0, 0, \
			 0, 0, 0, 0]

currStates = [0, 0, 0, 0, \
			 0, 0, \
			 0, 0, 0, 0]

#treeAmp, treeShift, carAmp, carShift, waveAmp, waveShift, leafAmp, leafShift
synthParams = [[0.5, 1],[0.5, 1],[0.5, 1],[0.5, 1]]
tree=0
car=1
wave=2
leaf=3
amp=0
shift=1

paramChange = 0.1

iterator = -1


class SampleListener():
	labels = ['wave_switch', 'wave_shift', 'wave_volume', \
	'urban_switch', 'urban_shift', 'urban_volume', \
	'chime_switch', 'chime_shift', 'chime_volume', \
	'bird_switch', 'bird_shift', 'bird_volume', \
	'wildcard_switch', 'wildcard_shift', 'wildcard_volume']
	#

	osc_client = None

	def add_osc_connect(self, client_connection):
		self.osc_client = client_connection
		print(self.osc_client)

	def sendOSC(self, val, content):
		if enable_osc:
			msg = OSC.OSCMessage()
			if val is 0:
				msg.setAddress("/Trees")
			elif val is 1:
				msg.setAddress("/Cars")
			elif val is 2:
				msg.setAddress("/Waves")
			elif val is 3:
				msg.setAddress("/Birds")
			for c in content:
				msg.append(c)
			self.osc_client.send(msg)


def parseSerial(serialData):
	splitSerial = serialData.split('--')
	parsed = []
	for val in splitSerial:
		parsed.append(int(val))
	return parsed

# def findDiffs(prev, curr):
# 	for old, new in prev, curr:
# 		if old is not new:


def main():
	global currStates
	global prevStates

	c = OSC.OSCClient()
	c.connect(('127.0.0.1', 57122))

	listener = SampleListener()
	listener.add_osc_connect(c)

	while True:
		try:
			# print("trying to receive data")
			serialData = ser.readline()
			print("serialData")
			print(serialData)
			prevStates = currStates
			currStates = parseSerial(serialData)
			# print(prevStates)
			# print(currStates)

			msg = []

			# Send OSC messages for four main sounds
			for i, val in enumerate(currStates[0:4]):
				#turn off
				if val is 0 and prevStates[i] is 1:
					msg = [0, currStates[6], currStates[7]]
					listener.sendOSC(i, msg)
					print(msg)

				if val is 1:
					# just changed states
					if prevStates[i] is 0:
						# send message for that state
						#turn on
						iterator=i
						synthParams[i][amp]=0.5
						synthParams[i][shift]=1
						msg = [1, synthParams[i][amp], synthParams[i][shift]
						listener.sendOSC(i, msg)
						print(msg)
					elif currStates[6] is not prevStates[6] or \
							currStates[7] is not prevStates[7]:

						#sustain
						if currStates[6] - prevStates[6] > 1000:
							synthParams[i][amp] += paramChange
						elif currStates[6] - prevStates[6] < -1000:
							synthParams[i][amp] -= paramChange

						if currStates[7] - prevStates[7] > 1000:
							synthParams[i][shift] += paramChange
						elif currStates[7] - prevStates[7] < -1000:
							synthParams[i][shift] -= paramChange

						msg = [2, synthParams[i][amp], synthParams[i][shift]]
						listener.sendOSC(i, msg)
						print(msg)
			if currStates[5] == 1:
				for i in range(4):
					iterator = (iterator+1)%4
					if currStates[iterator] == 1:
						break



			# listener.sendBirdOSC("header", currStates)
			# print("received data")
		except Exception as e:
			print(e)

if __name__ == "__main__":
	main()

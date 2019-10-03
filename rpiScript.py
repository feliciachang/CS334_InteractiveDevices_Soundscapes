#!/usr/bin/env python

#counter thingy for joystick that increments it downward

from time import sleep
import random
#random.randInt(0,high+1)
import sys
sys.path.insert(1, '/home/pi/pyosc')
from pythonosc.dispatcher import Dispatcher
dispatcher = Dispatcher()
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient
server = BlockingOSCUDPServer(("127.0.0.1", 57122), dispatcher)
client = SimpleUDPClient("127.0.0.1", 57122)
import serial # sudo pip install pyserial
import re
import gpiozero as gp

ser = serial.Serial('/dev/ttyAMA0', 9600)

#dispatcher = Dispatcher()

enable_osc = True

# Uses BCM pin numbering
chimePin = 17
carPin = 18
wavePin = 22
leafPin = 23
trfPin = 27

chimeLED = gp.LED(chimePin)
carLED = gp.LED(carPin)
waveLED = gp.LED(wavePin)
leafLED = gp.LED(leafPin)
trfLED = gp.LED(trfPin)

# chime, car, wave, leaf
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

#chimeAmp, chimeShift, carAmp, carShift, waveAmp, waveShift, leafAmp, leafShift
synthParams = [[0.5, 1],[0.5, 1],[0.5, 1],[0.5, 1]]
chimes = 0; car = 1; wave = 2; leaf = 3
tr = 4; iteratorIndex = 5;
amp = 0; shift = 1


paramChange = 0.1

iterator = -1

ampResting = 2675
shiftResting = 2915
# wildResting =


trfParamVals = [0.5, 0.5, 0.5, 1, 1, 10, 500, 0.001, 0.001, 0.5, 0.5]

#archetype: [index, valRangeMin, valRangeMax]
trfNumF=[0, 0, 1] #range 0-1
trfAmp1=[1, 0.1, 2.5] #range 0.1-2.5
trfAmp2=[2, 0.1, 2.5] #range 0.1-2.5
trfShift1=[3, 0.02, 4] #range 0.02 - 4
trfShift2=[4, 0.02, 4] #range 0.02 - 4
trfFreq1=[5, 1, 50] #range 1 - 50
trfFreq2=[6, 10, 1000] #range 10- 1000
trfGrainDur1=[7, 0.0001, 0.1] #range 0.0001 - 0.1
trfGrainDur2=[8, 0.0001, 0.1] #range 0.0001 - 0.1
trfVerbLvl1=[9, 0, 1] #range 0-1
trfVerbLvl2=[10, 0, 1] #range 0-1
trfParams = [trfNumF, trfAmp1, trfAmp2, trfShift1, trfShift2, trfFreq1, trfFreq2, \
trfGrainDur1, trfGrainDur2, trfVerbLvl1, trfVerbLvl2]


class SampleListener():
	labels = ['wave_switch', 'wave_shift', 'wave_volume', \
	'urban_switch', 'urban_shift', 'urban_volume', \
	'chime_switch', 'chime_shift', 'chime_volume', \
	'bird_switch', 'bird_shift', 'bird_volume', \
	'wildcard_switch', 'wildcard_shift', 'wildcard_volume']
	#

	#osc_client = None

	#def add_osc_connect(self, client_connection):
	#	self.osc_client = client_connection
	#	print(self.osc_client)

	def sendOSC(self, val, content):
		if enable_osc:

			if val is 0:
				label = "/Chimes"
			elif val is 1:
				label = "/Urban"
			elif val is 2:
				label = "/Waves"
			elif val is 3:
				label = "/Birds"
			elif val is 4:
				label = "/TechnoRainForest"

		client.send_message(label, content)


def parseSerial(serialData):
	splitSerial = serialData.split('--')
	parsed = []
	for val in splitSerial:
		parsed.append(int(val))
	return parsed

def resetParams(i):
	synthParams[i][amp] = 0.5
	synthParams[i][shift] = 1

def turnOnLED(led):
    if led is 0:
        chimeLED.on()
        carLED.off()
        waveLED.off()
        leafLED.off()
        #trfLED.off()
    elif led is 1:
        chimeLED.off()
        carLED.on()
        waveLED.off()
        leafLED.off()
        #trfLED.off()
    elif led is 2:
        chimeLED.off()
        carLED.off()
        waveLED.on()
        leafLED.off()
        #trfLED.off()
    elif led is 3:
        chimeLED.off()
        carLED.off()
        waveLED.off()
        leafLED.on()
        #trfLED.off()
    elif led is 4:
        chimeLED.off()
        carLED.off()
        waveLED.off()
        leafLED.off()
        #trfLED.on()

def main():
	global currStates
	global prevStates
	global iterator
	global trfParamVals
	global trfNumF
	global trfAmp1
	global trfAmp2
	global trfShift1
	global trfShift2
	global trfFreq1
	global trfGrainDur1
	global trfGrainDur2
	global trfVerbLvl1
	global trfVerbLvl2
	global trfParams

	#c = OSCClient()
	#c.connect(('127.0.0.1', 57122))

	listener = SampleListener()
	#listener.add_osc_connect(c)
	while True:
		print("work")

	# while True:
	# 		try:
    #         	turnOnLED(i)
    #         	print("starting code")
	#         # serialData = ser.readline()
	#         # print(serialData)
	# 		# prevStates = currStates
	# 	    # currStates = parseSerial(serialData)
	# 		#
	# 		# msg = []
	# 		#
	# 		# # Send OSC messages for four main sounds
	# 		# for i, val in enumerate(currStates[0:5]):
	# 		# 	# turn off
	# 		# 	if val is 0 and prevStates[i] is 1:
	# 		# 		msg = [0, currStates[6], currStates[7]]
	# 		# 		listener.sendOSC(i, msg)
	# 		#
	# 		# 	if val is 1:
	# 		# 		# turn on
	# 		# 		if prevStates[i] is 0:
	# 		#
	# 		# 			iterator = i
	# 		# 			turnOnLED(i)
	# 		# 			if i is 4:
	# 		# 				msg = [1]
	# 		# 				msg.extend(trfParamVals)
	# 		# 			else:
	# 		# 				resetParams(i)
	# 		# 				msg = [1, synthParams[i][amp], synthParams[i][shift]]
	# 		#
	# 		# 			listener.sendOSC(i, msg)
	# 		# 			print(msg)
	# 		# 		# sustain
	# 		# 		elif currStates[6] is not prevStates[6] or \
	# 		# 				currStates[7] is not prevStates[7]:
	# 		#
	# 		# 			if i is not 4:
	# 		#
	# 		# 				if currStates[6] - ampResting > 1000:
	# 		# 					if synthParams[i][amp] < 1:
	# 		# 						print('amp', synthParams[i][amp])
	# 		# 						synthParams[i][amp] += paramChange
	# 		# 				elif currStates[6] - ampResting < -1000:
	# 		# 					if synthParams[i][amp] > 0:
	# 		# 						print('amp', synthParams[i][amp])
	# 		# 						synthParams[i][amp] -= paramChange
	# 		#
	# 		# 				if currStates[7] - shiftResting > 1000:
	# 		# 					if synthParams[i][shift] < 4:
	# 		# 						print('shift', synthParams[i][shift])
	# 		# 						synthParams[i][shift] += paramChange
	# 		# 				elif currStates[7] - shiftResting < -1000:
	# 		# 					if synthParams[i][shift] > 0:
	# 		# 						print('shift', synthParams[i][shift])
	# 		# 						synthParams[i][shift] -= paramChange
	# 		#
	# 		# 				msg = [2, synthParams[i][amp], synthParams[i][shift]]
	# 		#
	# 		# 			else:
	# 		# 				if abs(currStates[8]-prevStates[8])>1000 or abs(currStates[9]-prevStates[9])>1000:
	# 		# 					for i in range(7):
	# 		# 						param = random.choice(trfParams)
	# 		# 						trfParamVals[param[0]] = random.uniform(param[1], param[2])
	# 		# 				msg = [2]
	# 		# 				msg.extend(trfParamVals)
	# 		# 			listener.sendOSC(i, msg)
	# 		#
	# 		#
	# 		# if currStates[iteratorIndex] == 1:
	# 		# 	for i in range(4):
	# 		# 		iterator = (iterator+1)%4
	# 		# 		if currStates[iterator] == 1:
	# 		# 			turnOnLED(i)
	# 					break
	#
	#
	# 		# listener.sendBirdOSC("header", currStates)
	# 		# print("received data")
	# 	except Exception as e:
	# 		print(e)

if __name__ == "__main__":
	main()

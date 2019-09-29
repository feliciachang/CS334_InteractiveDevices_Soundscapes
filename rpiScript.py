#counter thingy for joystick that increments it downward

from time import sleep
import OSC
import serial
import re
ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 9600)

enable_osc = True

# tree, car, wave, leaf
# wildcard, iterate
# amp, shift, wildX, wildY

prevStates = [0, 0, 0, 0, \
			 0, 0, \
			 0, 0, 0, 0]

currStates = [0, 0, 0, 0, \
			 0, 0, \
			 0, 0, 0, 0]

# const int TreeButton = 0;
# const int CarSwitch = 22;
# const int WaveButton = 21;
# const int LeafSwitch = 0;
# const int WildSwitch = 0;
# const int iterate = 0;
#
# const int amp = 25;
# const int shift = 26;
# const int wildcardX = 0;
# const int wildcardY = 0;

class SampleListener():
	labels = ['wave_switch', 'wave_shift', 'wave_volume', \
	'urban_switch', 'urban_shift', 'urban_volume', \
	'chime_switch', 'chime_shift', 'chime_volume', \
	'bird_switch', 'bird_shift', 'bird_volume', \
	'wildcard_switch', 'wildcard_shift', 'wildcard_volume']
	#
	# playBird = 0
	# playTree = 0
	# playCar = 0
	# playWave = 0
	# playWildcard = 0
	# volume = 0
	# currentObj = 0
	osc_client = None

	def add_osc_connect(self, client_connection):
		self.osc_client = client_connection
		print(self.osc_client)

	def sendBirdOSC(self, header, content):
		if enable_osc:
			msg = OSC.OSCMessage()
			msg.setAddress("/Birds")
			for c in content[0:3]:
				msg.append(c)
			self.osc_client.send(msg)

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
				if val is 0 and prevStates[i] is 1:
					msg = [0, prevStates[6], prevStates[7]]
					listener.sendOSC(i, msg)
					print(msg)

				if val is 1:
					# just changed states
					if prevStates[i] is 0:
						# send message for that state
						msg = [1, currStates[6], currStates[7]]
						listener.sendOSC(i, msg)
						print(msg)
					elif currStates[6] is not prevStates[6] or \
							currStates[7] is not prevStates[7]:

						msg = [2, currStates[6], currStates[7]]
						listener.sendOSC(i, msg)
						print(msg)


			# listener.sendBirdOSC("header", currStates)
			# print("received data")
		except Exception as e:
			print(e)

if __name__ == "__main__":
	main()

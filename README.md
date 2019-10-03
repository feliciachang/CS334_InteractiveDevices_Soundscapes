# CS334_InteractiveDevices_Soundscapes
Task two of the interactive Devices module

# "Nature Valley": a modular soundscape

Nature Valley is a modular soundscape that allows users to customize ambient sounds. 
Users can mix and match four soundscapes: urban noise, bird sounds, wind chimes, waves, and "techno" rainforests with the additional ability to manipulate pitch and amplitude for each sound. The form factor of Nature Valley is designed so to replicate the natural movement of the sound in real life: push the wave down to hear waves crash on rocks, pull a car to hear urban sounds, lift a leaf up to uncover a bird chirping, etc. 

# Buidling a Nature Valley

## Replicating the Nature Valley Software
To build the Nature Valley Software, you will need to have installed:
- the Arduino IDE
- SuperCollider
- Python and PyOSC

and git clone this repository

## Understanding the SuperCollider code
In the SuperCollider file, you will find the .wav files for each ambient noise. In the SuperCollider program, Soundscapes.scd, these sounds become synths that can be manipulated by pitch and amplitude. 
Input to each synth is sent through OSC listeners. There is one listener per synth. 

You may change your ambient sounds simply by changing the .wav files. 
You may also add and delete as many synths as you'd like as long as changes are also mapped to the Arduino and Python code. 

## Understanding the Arduino code
The Arduino code can be found in the folder PushButtonParsed as PushButtonParsed.ino 

The physical pins for each joystick, switch, and button, is marked as constants. You can change where the pin values for each controller as long as you also change the value of the constant.
The Arduino code records activity from each controller and sends the data in one string to the python script, rpiscript.py. 

## Understanding the Python script
The python script that bridges Arduino input and SuperCollider functionality is called rpiscript.py. 
The script parses through string input in the Ardunio and records the data as a state. It then compares the current state to the previous state to determine what data has changed. The relevant data is then passed to SuperCollider with OSC.

## Replicating the Nature Valley Hardware
To build the physical Nature Valley device, you will need the following materials:
- three joysticks
- three buttons 
- three switches
- four LED lights
- breadboard
- raspberry pi 3B+
- ESP32
- wood
- lego
- paint
- Many many wires

## Building the Nature Valley Exterior
Building the facade of Nature Valley, will require some sculptural and woodworking expertise.
The wave, car, and three created by combining cross sections a sillhouette of the object together by glue. The other objects were more sculptural and can be be made with your own creative agency. The bird is essentially a ball of fluff while the leaf is a wire with cloth. 
Each symbol is then mounted on a __x__ plane making a ___ length rectangle. This is the length of the box. The depth of the box is __.




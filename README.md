# CS334_InteractiveDevices_Soundscapes
Task two of the interactive Devices module

# "Nature Valley": a modular soundscape

Nature Valley is a modular soundscape that allows users to customize ambient sounds. 
Users can mix and match four soundscapes: urban noise, bird sounds, wind chimes, waves, each of which use sound samples, and a handcrafted synth best described as a "techno rainforest". Users have the additional ability to manipulate the pitch and amplitude for each sound. The form factor of Nature Valley is designed so as to replicate the natural motions which create each sound in real life: push the wave down to hear the ocean crashing on rocks, pull a car down the road to hear urban sounds, lift a leaf up to uncover a bird chirping, etc. 

## Replicating the Nature Valley Software
To build the Nature Valley Software, you will need to have installed:
- the Arduino IDE
- SuperCollider
- Python and PyOSC

and git clone this repository

## Understanding the SuperCollider code
In the SuperCollider file, you will find the .wav files for each ambient noise. In the SuperCollider program, Soundscapes.scd, these sounds become synths that can be manipulated by pitch and amplitude. 
Input to each synth is sent through OSC listeners. There is one listener per synth. 
These listeners parse messages sent from Python and run, end or change the argument values for each ambient sound. 
You may change your ambient sounds simply by changing the .wav files. 
You may also add and delete as many synths as you'd like as long as changes are also mapped to the Arduino and Python code. 

## Understanding the Arduino code
The Arduino code can be found in the folder PushButtonParsed as PushButtonParsed.ino. This code is flashed onto an ESP32 microcontroller.

The physical esp32 gpio pins for each joystick, switch, and button, are marked as constants. You can change the pin values for each controller as long as you also change the value of the constant.
The Arduino code records activity from each controller and sends the data through serial protocol as one string to the python script, rpiscript.py. 

## Understanding the Python script
The python script that bridges Arduino's serial data and SuperCollider functionality is called rpiscript.py. 
The script parses the string output from the Arduino and records the data as a current state array. It then compares the current state to the previous state to determine what data has changed. The relevant data is then passed to SuperCollider with OSC.

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
The wave, car, and tree are made of 1/4" sheet wood. A number of section cuts of the objects are conjoined with wood glue to achieve adequate thickness. The bird/leaf interface is more sculptural and can be be made with your own creative agency. Our bird is a decorated puff ball while the leaf is a wire armature and stained cloth.
Each diorama is then mounted on a 5" x 7" rectangle of 1/4" wood, along with one extra 5" x 7" rectangle for the controlers, making a 25" x 7" rectangle.
To achieve the falling motion of the wave, the model is attached to its base with a hinge, and a rubber band attaches it on the back to its base, drawing it back to standing position after it is pushed down.
To achieve the swaying of the tree and its chimes, a screw is connected into the bottom of the tree through a hole in the platform slightly larger than the guage of the screw but smaller than the width of the screw's head and than the base of the tree.
To achieve the sliding of the car, slots are cut into the car's platform to allow wooden tabs on the bottom of the car to extend below the surface of the platform. Cardboard is then used to connect the wooden tabs below the rectangle. 
To achieve the rise and fall of the leaf over the bird, the wire stem of the leaf is affixed directly to a switch, which in turn is held against a wooden wall behind the bird.
Walls are built down from this extended surface of moveable models to create a box with depth 4".

## The Nature Valley Interior
Inside the hollow space of the box, the pi, the ESP32, and all the wiring are held together. The boards are placed in stabilizing structures made of Legos and hot glue. The wires are labeled with Sharpie on masking tape tabs, bunched and in clear paths affixed to the inside walls using duct tape.

## Autostart on the Raspberry Pi
An intermediary supercollider file called init.scd is added to the Desktop directory of the pi. In it is just a link to the main supercollider document. The pi's chron file is then edited to schedule a command to sclang to run init.scd 20 seconds after boot.
The pi's rc.local file is then edited to run the python script on boot.

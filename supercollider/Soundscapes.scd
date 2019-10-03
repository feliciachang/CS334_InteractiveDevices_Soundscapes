s.boot;

s.waitForBoot{

	~waveSounds = Buffer.read(s, "Ocean_Waves.wav".resolveRelative);
	~urbanSounds = Buffer.read(s, "Times_Square.wav".resolveRelative);
	~chimeSounds = Buffer.read(s, "Wind_Chimes.wav".resolveRelative);
	~birdSounds = Buffer.read(s, "Bird_Songs.wav".resolveRelative);


	//shift must be between 0 and 4
	SynthDef(\waves, {|amp=0.5, shift =1|
		Out.ar(0, PitchShift.ar(PlayBuf.ar(1, ~waveSounds, loop:1)*amp, 0.01, shift)!2);
	}).add;

	SynthDef(\urban, {|amp=0.5, shift=1|
		Out.ar(0, PitchShift.ar(PlayBuf.ar(1, ~urbanSounds, loop:1)*amp, 0.01, shift)!2);
	}).add;

	SynthDef(\chimes, {|amp=0.5, shift=1|
		Out.ar(0, PitchShift.ar(PlayBuf.ar(1, ~chimeSounds, loop:1)*amp, 0.01, shift)!2);
	}).add;

	SynthDef(\birds, {|amp=0.5, shift=1|
		Out.ar(0, PitchShift.ar(PlayBuf.ar(1, ~birdSounds, loop:1)*amp!2, 0.01, shift)!2);
	}).add;

	SynthDef(\technoRainForest, {|amp1=0.5, amp2=0.2, shift1=0.2, shift2=0.3, freq1 = 10, freq2 = 500, grainDur1=0.001, grainDur2 = 0.001, numF=0.5, verblvl1=0.5, verblvl2=0.5|
		Out.ar(0, Mix.ar([FreeVerb.ar(PitchShift.ar((GrainSin.ar(2, Impulse.kr(freq1), grainDur1, BrownNoise.kr.range(1, 50000), 0))*3, 0.01, shift1), room:verblvl1) * amp1, numF* FreeVerb.ar(PitchShift.ar((GrainSin.ar(2, GbmanL.ar(freq2, 1.2, 2.1), grainDur2, BrownNoise.kr.range(1, 50000)))*3, 0.01, shift2), room:verblvl2)*amp2]));
	}).add;


	s.sync;

	//how is it getting turn on/off data? Is python preprocessing, so msg[0] ==1 means turn on, which will never coincide with msg[1]==1, which means turn off? msg[2] is volume, msg[3] is shift
	~chimesListener = OSCFunc( { | msg, time, addr, port |
		postln("OSC received in SC");
		postln(msg);
		case
		{msg[1] == 1} {
			postln("ON");
			~chimes = Synth(\chimes);
		}
		{msg[1] == 0} {
			postln("OFF");
			~chimes.free;
		}
		{msg[1] == 2} {
			postln("SUSTAIN");
			~chimes.set(\amp, msg[1]);
			~chimes.set(\shift, msg[2]);
		};
	}, '\Chimes', recvPort: 57122);

	~urbanListener = OSCFunc( { | msg, time, addr, port |
		postln("OSC received in SC");
		postln(msg);
		case
		{msg[1] == 1} {
			postln("ON");
			~urban = Synth(\urban);
		}
		{msg[1] == 0} {
			postln("OFF");
			~urban.free;
		}
		{msg[1] == 2} {
			postln("SUSTAIN");
			~urban.set(\amp, msg[1]);
			~urban.set(\shift, msg[2]);
		};
	}, '\Urban', recvPort: 57122);

	~wavesListener = OSCFunc( { | msg, time, addr, port |
		postln("OSC received in SC");
		postln(msg);
		case
		{msg[1] == 1} {
			postln("ON");
			~waves = Synth(\waves);
		}
		{msg[1] == 0} {
			postln("OFF");
			~waves.free;
		}
		{msg[1] == 2} {
			postln("SUSTAIN");
			~waves.set(\amp, msg[1]);
			~waves.set(\shift, msg[2]);
		};
	}, '\Waves', recvPort: 57122);


	~birdsListener = OSCFunc( { | msg, time, addr, port |
		postln("OSC received in SC");
		postln(msg);
		case
		{msg[1] == 1} {
			postln("ON");
			~birds = Synth(\birds);
		}
		{msg[1] == 0} {
			postln("OFF");
			~birds.free;
		}
		{msg[1] == 2} {
			postln("SUSTAIN");
			~birds.set(\amp, msg[1]);
			~birds.set(\shift, msg[2]);
		};
	}, '\Birds', recvPort: 57122);

	~tRFListener = OSCFunc( { | msg, time, addr, port |
		postln("OSC received in SC");
		postln(msg);
		case
		{msg[1] == 1} {
			postln("ON");
			~tRF = Synth(\technoRainForest);
		}
		{msg[1] == 0} {
			postln("OFF");
			~tRF.free;
		}
		{msg[1] == 2} {
			postln("SUSTAIN");
			~tRF.set(\numF, msg[2]);
			~tRF.set(\amp1, msg[3]);
			~tRF.set(\amp2, msg[4]);
			~tRF.set(\shift1, msg[5]);
			~tRF.set(\shift2, msg[6]);
			~tRF.set(\freq1, msg[7]);
			~tRF.set(\freq2, msg[8]);
			~tRF.set(\grainDur1, msg[9]);
			~tRF.set(\grainDur2, msg[10]);
			~tRF.set(\verblvl1, msg[11]);
			~tRF.set(\verblvl2, msg[12]);
		};
	}, '/TechnoRainForest', recvPort: 57122);

	//as either grainDur goes above 0.01, corresponding amp should go below 0.07


	// x=Synth(\birds);
	/*m = Synth(\wildCard);
	m.set(\numF, 0.0);
	m.set(\shift2,0.03);
	m.set(\amp1, 0.9);
	m.set(\grainDur1, 0.001);
	m.set(\freq1, 300);
	m.set(\shift1, 0.1);
	m.set(\freq2, 500);
	m.set(\amp2, 0.3);
	m.set(\grainDur2, 0.01);*/



	/*x.set(\rQ, 0.1);
	x.set(\shift, 4);
	x.set(\freq, 2000);
	x.set(\freq, 100);
	x.set(\amp, 1.5);
	x.free;
	y= Synth(\urban);
	y.set(\shift, 1);
	y.free;*/
};

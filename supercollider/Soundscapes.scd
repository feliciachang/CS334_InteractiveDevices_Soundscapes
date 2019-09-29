s.quit;
s.boot;

s.waitForBoot{
	(
		~waveSounds = Buffer.read(s, "ocean.wav".resolveRelative);
		~urbanSounds = Buffer.read(s, "car.wav".resolveRelative);
		~chimeSounds = Buffer.read(s, "chimes.MP3".resolveRelative);
		~birdSounds = Buffer.read(s, "cranes.wav".resolveRelative);
	)

	/*(
		~waveSounds.free;
		~urbanSounds.free;
		~chimeSounds.free;
		~birdSounds.free;
	)*/
	(
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

	/*	SynthDef(\wildCard, {|amp1=0.5, amp2=0.2, shift1=0.2, shift2=0.3, freq1 = 10, freq2 = 500, grainDur1=0.001, grainDur2 = 0.001, filterWidth, numF=0.5, verblvl1=0.5, verblvl2=0.5|
			Out.ar(0, Mix.ar([FreeVerb.ar(PitchShift.ar((SinGrain.ar(Impulse.kr(freq1), grainDur1, BrownNoise.kr.range(1, 50000)))*3, 0.01, shift1), room:verblvl1) * amp1, numF* FreeVerb.ar(PitchShift.ar((SinGrain.ar(GbmanL.ar(freq2, 1.2, 2.1), grainDur2, BrownNoise.kr.range(1, 50000)))*3, 0.01, shift2), room:verblvl2)*amp2]));
	}).add;*/

	)
	//x = Synth(\birds);

	//how is it getting turn on/off data? Is python preprocessing, so msg[0] ==1 means turn on, which will never coincide with msg[1]==1, which means turn off? msg[2] is volume, msg[3] is shift
	~chimesListener = OSCFunc( { | msg, time, addr, port |
		postln("OSC received in SC");
		postln(msg);
		if(asInt(msg[1]) == 1, {
			postln("entered if");
			~chimes = Synth(\chimes);
			//~chimes.set(\amp, msg[1]);
			//~chimes.set(\shift, msg[2]);
		},
		{
			postln("else didn't work");
			~chimes.free;
		});
	}, '\Chimes', recvPort: 57122);

	~urbanListener = OSCFunc( { | msg, time, addr, port |
		postln("OSC received in SC");
		postln(msg);
		if(asInt(msg[1]) == 1, {
			postln("entered if");
			~urban = Synth(\urban);
			//~urban.set(\amp, msg[1]);
			//~urban.set(\shift, msg[2]);
		},
		{if (msg[1] == 0, {
			postln("else didn't work");
			~urban.free;
		}, {
			~urban.set(\amp, msg[1]);
			~urban.set(\shift, msg[2]);
		})});
	}, '\Urban', recvPort: 57122);

	~wavesListener = OSCFunc( { | msg, time, addr, port |
		postln("OSC received in SC");
		postln(msg);
		case
		{msg[1] == 1} {
			postln("entered if");
			~waves = Synth(\waves);
		}
		{msg[1] == 0} {
			postln("else didnt work")
			~waves.free;
		}
		{msg[1] == 2} {
			~waves.set(\amp, msg[1]);
			~waves.set(\shift, msg[2]);
		};
	}, '\Waves', recvPort: 57122);



/*		if(asInt(msg[1]) == 1, {
			postln("entered if");
			~waves = Synth(\waves);
			//~urban.set(\amp, msg[1]);
			//~urban.set(\shift, msg[2]);
		},
		{if(msg[1] == 0, {
			postln("else didn't work");
			~waves.free;
		}, {
			~waves.set(\amp, msg[1]);
			~waves.set(\shift, msg[2]);
		})});*/

	~birdsListener = OSCFunc( { | msg, time, addr, port |
		postln("OSC received in SC");
		postln(msg);
		if(asInt(msg[1]) == 1, {
			postln("entered if");
			~birds = Synth(\birds);
			//~birds.set(\amp, msg[1]);
			//~birds.set(\shift, msg[2]);
		},
		{
			postln("else didn't work");
			~birds.free;
		});
	}, '\Birds', recvPort: 57122);

	//as either grainDur goes above 0.01, corresponding amp should go below 0.07


	x=Synth(\birds);
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

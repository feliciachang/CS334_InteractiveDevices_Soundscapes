(
s.boot;
~waveSounds = Buffer.read(s, "ocean.wav".resolveRelative);
~urbanSounds = Buffer.read(s, "car.wav".resolveRelative);
~chimeSounds = Buffer.read(s, "chimes.MP3".resolveRelative);
~birdSounds = Buffer.read(s, "cranes.wav".resolveRelative);
)

(
~waveSounds.free;
~urbanSounds.free;
~chimeSounds.free;
~birdSounds.free;
)
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
	Out.ar(0, PitchShift.ar(PlayBuf.ar(1, ~birdSounds, loop:1)*amp, 0.01, shift)!2);
}).add;

)
x = Synth(\birds);

(
SynthDef(\wildCard, {|amp1=0.5, amp2=0.2, shift1=0.2, shift2=0.3, freq1 = 10, freq2 = 500, grainDur=0.001, filterWidth, numF=0.5|
	Out.ar(0, Mix.ar([FreeVerb.ar(PitchShift.ar((SinGrain.ar(Impulse.kr(freq1), grainDur, BrownNoise.kr.range(1, 50000)))*3, 0.01, shift1)), numF* FreeVerb.ar(PitchShift.ar((SinGrain.ar(GbmanL.ar(500, 1.2, 2.1), 0.001, BrownNoise.kr.range(1, 50000)))*3, 0.01, shift2))*amp2]));
}).add;)

m = Synth(\wildCard);
m.set(\numF, 0.2);
m.set(\shift2, 0.1);
m.set(\amp1, 1);
m.set(\grainDur, 0.0001);


//play({BrownNoise.ar * SinGrain.ar(});
play({HPF.ar(FreeVerb.ar(PitchShift.ar((SinGrain.ar(Impulse.kr(10), 0.001, WhiteNoise.kr.range(1, 50000)))*2, 0.01, 1)), 8000)});

play({FreeVerb.ar(PitchShift.ar((SinGrain.ar(GbmanL.ar(50, 1.2, 2.1), 0.001, BrownNoise.kr.range(1, 50000)))*2, 0.01, 1))});

play({FreeVerb.ar(PitchShift.ar((SinGrain.ar(Impulse.kr(10), 0.001, BrownNoise.kr.range(1, 50000)))*2, 0.01, 0.2))});

/*(
play({
	Mix.ar(FreeVerb.ar(PitchShift.ar((SinGrain.ar(Impulse.kr(10), 0.001, BrownNoise.kr.range(1, 50000))), 0.01, 0.2))+FreeVerb.ar(PitchShift.ar((SinGrain.ar(GbmanL.ar(1000, 1.2, 2.1), 0.001, BrownNoise.kr.range(1, 50000))), 0.01, 1)));
})
)*/


x.set(\rQ, 0.1);
x.set(\shift, 4);

x.set(\freq, 2000);

x.set(\freq, 100);

x.set(\amp, 1.5);

x.free;

y= Synth(\urban);
y.set(\shift, 1);
y.free;
(
play({
    z = Blip.ar(200, 6, 0.1);
    PitchShift.ar(z, 0.01, 0.1, 0, 0.0001)
}))

play({Blip.ar(200, 6, 0.1)});
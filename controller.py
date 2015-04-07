#! /usr/bin/env python2

import sys, subprocess, time
from aubio import source, pitch, freqtomidi
from pysoundcard import Stream   

if len(sys.argv) < 2:
    print "Usage: %s <filename> [samplerate]" % sys.argv[0]
    sys.exit(1)

filename = sys.argv[1]
downsample = 1
samplerate = 44100 / downsample
if len( sys.argv ) > 2: samplerate = int(sys.argv[2])
win_s = 1024 / downsample # fft size 4096
hop_s = 100 / downsample # hop size 512

# Pitch detection
tolerance = 0.8
pitch_o = pitch("yin", win_s, hop_s, samplerate)
pitch_o.set_unit("freq")
pitch_o.set_tolerance(tolerance)

while True:
    # Input
    s = source(filename, samplerate, hop_s)
    samplerate = s.samplerate
    
    # Ouput
    #f = Stream(sample_rate=samplerate, block_length=hop_s, input_device=False)
    #f.start()

    pitches = []
    confidences = []

    # total number of frames read
    total_frames = 0

    # Play the audio
    subprocess.Popen(["aplay", filename])
    allsamples = []
    while True:
        samples, read = s()
        #f.write(samples) 
        pitch = pitch_o(samples)[0]
        #pitch = int(round(pitch))
        confidence = pitch_o.get_confidence()
        #if confidence < 0.8: pitch = 0.
        #print "%f %f %f" % (total_frames / float(samplerate), pitch, confidence)
        #print(pitch)
        pitches += [pitch]
        confidences += [confidence]
        total_frames += read
        time.sleep(0.01)
        if read < hop_s: break
    print('FINISHED')
    time.sleep(1)
    #f.stop()

if 0: sys.exit(0)

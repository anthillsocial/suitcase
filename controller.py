#! /usr/bin/env python2
import sys, subprocess, time
from aubio import source, pitch, freqtomidi
from pysoundcard import Stream   

# Check if we have been passed a filename
if len(sys.argv) < 2:
    print "Usage: %s <filename> [samplerate]" % sys.argv[0]
    sys.exit(1)

# Setup some base variables
filename = sys.argv[1]
downsample = 1
samplerate = 44100 / downsample
if len( sys.argv ) > 2: samplerate = int(sys.argv[2])
win_s = 1024 / downsample # fft size 4096
hop_s = 100 / downsample # hop size 512

def subproc(cmd):
    #string = subprocess.getoutput(cmd, shell=True).decode("utf-8").strip()
    string = subprocess.check_output(cmd, shell=True).strip()
    return string

# Lets get some details on the .wav file
seconds = float(subproc("sox --i -D tones.wav "))
nsamples = int(subproc("sox --i -s tones.wav"))
print("seconds:'{}' samples:'{}'".format(seconds, nsamples))

# Pitch detection vars
tolerance = 0.8
pitch_o = pitch("yin", win_s, hop_s, samplerate)
pitch_o.set_unit("freq")
pitch_o.set_tolerance(tolerance)

# Play the sample on loop
while True:
    # Input
    s = source(filename, samplerate, hop_s)
    samplerate = s.samplerate

    # total number of frames read
    total_frames = 0

    # Play the audio
    subprocess.Popen(["aplay", filename])
    allsamples = []

    startloop = time.time()
    oldpitch = -1
    print(startloop)
    while True:
        elapsed = startloop-time.time()
        samples, read = s()
        total_frames += read
        pitch = pitch_o(samples)[0]
        pitch = int(round(pitch))
        if pitch != oldpitch:
            pass
        thetime=time.time() 
        elapsed = thetime - startloop
        print("pitch:{} time:{} elapsed:{} totalframes:{} ".format(pitch, thetime, elapsed, total_frames))
        oldpitch = pitch
        time.sleep(0.25)
        if read < hop_s: break
    elapsed = time.time()-startloop
    print('FINISHED elapsed:{} nFrames:{}'.format(elapsed, total_frames))
    pause = seconds-elapsed
    if pause <=0:
        time.sleep(1)
    else:
        print("Auto pause")
        time.sleep(pause+1)

if 0: sys.exit(0)

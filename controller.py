#! /usr/bin/env python2
##############################################
# Plays an audio file and determins frequency
##############################################
import sys, subprocess, time

def startup():
    # Check if we have been passed a filename
    if len(sys.argv) < 2:
        print "Usage: %s <filename> [samplerate]" % sys.argv[0]
        sys.exit(1)
    filename = sys.argv[1]
    leftchannel = grableftchannel(filename)
    rightchannel = grabrightchannel(filename)
    scanfile(filename, leftchannel, rightchannel)

def generatecommand(pitch):
    sens = 40 # sensitivity
    if inrange(pitch, 400, sens): print('Forward: {}'.format(pitch))
    if inrange(pitch, 500, sens): print('Backward: {}'.format(pitch))
    if inrange(pitch, 600, sens): print('Stop: {}'.format(pitch))
    if inrange(pitch, 700, sens): print('Stop2: {}'.format(pitch))
    if inrange(pitch, 1500, 500): print('set speed: {}'.format(pitch))

# Is this pitch within a certain range
def inrange(pitch, target, sens):
    if pitch<=target+sens and pitch>=target-sens:
        return True
    else:
        return False

def grableftchannel(filename):
    leftchannelfile = "L"+filename
    subprocess.Popen(["sox", filename, leftchannelfile, "remix", "1"])
    return leftchannelfile

def grabrightchannel(filename):
    rightchannelfile = "R"+filename
    subprocess.Popen(["sox", filename, rightchannelfile, "remix", "1"])
    return rightchannelfile

# Scan a file for pitch, play it back
def scanfile(filename, leftchannelfile, rightchannelfile):
    from aubio import source, pitch, freqtomidi
   
    # Setup some base variables
    downsample = 1
    samplerate = 44100 / downsample
    if len( sys.argv ) > 2: samplerate = int(sys.argv[2])
    win_s = (1024*3) / downsample # fft size 4096
    hop_s = 512 / downsample # hop size 512

    # Pitch detection vars
    tolerance = 0.8
    pitch_o = pitch("yin", win_s, hop_s, samplerate)
    pitch_o.set_unit("freq")
    pitch_o.set_tolerance(tolerance)

    # Lets get some details on the .wav file
    seconds = float(subproc("sox --i -D {}".format(filename)))
    nsamples = int(subproc("sox --i -s {}".format(filename)))
    secondspersample = seconds/nsamples
    print("seconds:'{}' samples:'{}' secondspersample:{}".format(seconds, nsamples, secondspersample))

    # Play the sample on loop
    while True:
        # Input
        s = source(leftchannelfile, samplerate, hop_s)
        samplerate = s.samplerate

        # total number of frames read
        total_frames = 0

        # Play the audio
        subprocess.Popen(["aplay", leftchannelfile])
        
        # Time we started
        startloop = time.time()
        oldpitch = -1
        
        # Scan and play the sample on a loop
        while True:
            # Read the samples
            samples, read = s()
            total_frames += read
            # Work out the pitch
            pitch = pitch_o(samples)[0]
            pitch = int(round(pitch))
            if pitch != oldpitch:
                #print("=======pitch:{}".format(pitch))
                generatecommand(pitch)
            oldpitch = pitch 
            # Work out how much time should have passed
            thetime = time.time() 
            elapsed = thetime-startloop
            targettime = total_frames*secondspersample
            # And pause in order to kepp in sync
            pause = targettime-elapsed
            if pause > 0:
                time.sleep(pause)
            #print("pitch:{} time:{} elapsed:{} totalframes:{} ".format(pitch, thetime, elapsed, total_frames))
            # Have we reached then end of the audio file
            if read < hop_s: break
        elapsed = time.time()-startloop
        #print('FINISHED elapsed:{} nFrames:{}'.format(elapsed, total_frames))
        pause = seconds-elapsed
        if pause >0:
            time.sleep(pause+0.5)

# Grab output from the commandline
def subproc(cmd):
    string = subprocess.check_output(cmd, shell=True).strip()
    return string


startup()
if 0: sys.exit(0)

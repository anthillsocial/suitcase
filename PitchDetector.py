#!/usr/bin/python2
# Tom Keene 2015 ww.theanthillsocial.co.uk 
# For Kypros Kyrianou: http://electronicsunset.org
# Script forked from:
# http://chrisbaume.wordpress.com/2013/02/09/aubio-alsaaudio/
###########################################################################

import alsaaudio, struct
from aubio.task import *

class PitchDetector:
    
    def __init__(self, callback): 
        # Callback function
        self.callback = callback
        # constants
        CHANNELS    = 1
        INFORMAT    = alsaaudio.PCM_FORMAT_FLOAT_LE
        RATE        = 44100
        FRAMESIZE   = 1024
        PITCHALG    = aubio_pitch_yin
        PITCHOUT    = aubio_pitchm_freq
        # set up audio input
        self.recorder = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)
        self.recorder.setchannels(CHANNELS)
        self.recorder.setrate(RATE)
        self.recorder.setformat(INFORMAT)
        self.recorder.setperiodsize(FRAMESIZE)
        # set up pitch detect
        self.detect = new_aubio_pitchdetection(FRAMESIZE,FRAMESIZE/2,CHANNELS,
                                        RATE,PITCHALG,PITCHOUT)
        self.buf = new_fvec(FRAMESIZE,CHANNELS)
        self.loop()

    def loop(self):
        # main loop
        while True:
            # read data from audio input
            [length, data]=self.recorder.read()
            # convert to an array of floats
            #floats = struct.unpack('f'*FRAMESIZE,data)
            floats = struct.unpack('f'*length,data)
            # copy floats into structure
            for i in range(len(floats)):
                fvec_write_sample(self.buf, floats[i], 0, i)
            # find pitch of audio frame
            freq = aubio_pitchdetection(self.detect,self.buf)
            # find energy of audio frame
            energy = vec_local_energy(self.buf)
            string = "{:10.4f} {:10.4f}".format(freq,energy)
            self.callback(freq, energy)
 
if __name__ == "__main__": 
    def setmotor(pitch):
        print(pitch)

    pitcher = PitchDetector(setmotor)
        


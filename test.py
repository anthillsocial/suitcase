import time, wave, pymedia.audio.sound as sound
f= wave.open( 'tones.wav', 'rb' )
sampleRate= f.getframerate()
channels= f.getnchannels()
format= sound.AFMT_S16_LE
snd= sound.Output( sampleRate, channels, format )
s= f.readframes( 300000 )
snd.play( s )

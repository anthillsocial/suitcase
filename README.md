# Suitcase
Stepper motor controlled by audio frequency using a RAspberry Pi. 
Created 2016 for Kypros Kyprianou: www.electronicsunset.org
Released under a GPL Licence unless otherwise stated. 

The code (in development):

Analyses audio pitch and controls a stepper motor in respoinse to specific frequencies. 

## The hardware

- Raspbery Pi 2
- Getbot Rpi stepper motor controller board. 
- 12V, 1.7A, 667oz-in NEMA-17 Bipolar Stepper Motor
- 8mm Set Screw Hub

## Prepare the Raspberry Pi 2 On Rapbian Wheezy
Follow audio setup istructions here:
https://sites.google.com/site/observing/Home/speech-recognition-with-the-raspberry-pi

Then install aubio:
	
	sudo apt-get install python python-alsaaudio python-aubio

And run the suitcase script:
	
	./suitcase

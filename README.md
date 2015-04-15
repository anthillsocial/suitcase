# suitcase
Stepper motor controlled by audio frequency

## The hardware
All ordered from www.robotShop.com

- Raspbery Pi 2
- DRV8825 Stepper Motor Driver Breakout Board
- 12V, 1.7A, 667oz-in NEMA-17 Bipolar Stepper Motor
- 8mm Set Screw Hub

## Prepare the Raspberry Pi 2
*SD card setup*
Follow these instructions for preparing an SD card, be carefull not to wipe your own hard drive!:
www.archlinuxarm.org/platforms/armv7/broadcom/raspberry-pi-2

*Direct connection over ethernet*
TODO

## Prepare the software

    git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
    pacman -S libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev

## Install python module: pyaudo

    pacman -S python-pip
    pip install pyaudio --allow-external pyaudio --allow-unverified pyaudio
    pacman -S python-numpy
    pacman -S alsa-utils

## Install python module: pyaubio
    pacman -S aubio
    pip install pysoundcard
    sudo cp /usr/lib/python3.4/site-packages/pysoundcard.py /usr/lib/python2.7/site-packages/pysoundcard.py
    pacman -S python2-cffi

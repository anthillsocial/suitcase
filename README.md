# suitcase
Stepper motor controlled by audio frequency using a RAspberry Pi. Created for Kypros Kypriano: www.electronicsunset.org
Released under a GPL V2 Licence. 

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

I used the follwowing commands on ARch Linux:

    fdisk /dev/mmcblk0

At the prompt:

    a. Type o | This will clear out any partitions on the drive.
    b. Type p | to list partitions. There should be no partitions left.
    c. Type n | 
    d. Then p | for primary
    e. Then 1 | for the first partition on the drive
    f. Then ENTER | To accept the default first sector
    g. Then type: +100M | for the last sector.  
    h. Then t |
    i. Then c | set the first partition to type W95 FAT32 (LBA).
    j. Then n | 
    k. TThen p | for primary
    l. Then 2 | for the second partition on the drive, and then press 
    m. ENTER | accept the default first 
    n. ENTER | accept default last sector.
    o. Then w | write the partition table and exit by typing w.

Finally create and mount the filesystem:

    mkfs.vfat /dev/mmcblk0p1
    mkdir boot
    mount /dev/mmcblk0p1 boot

    mkfs.ext4 /dev/mmcblk0p2
    mkdir root
    mount /dev/mmcblk0p2 root

    wget http://archlinuxarm.org/os/ArchLinuxARM-rpi-2-latest.tar.gz
    bsdtar -xpf ArchLinuxARM-rpi-2-latest.tar.gz -C root
    sync

    mv root/boot/* boot
    umount boot root

## Prep Arch linux on Raspberry Pi
Once the sd card has been setup, then the system needs some tweeks so we can get going, 
such as auto-connecting to a wifi network so we can ssh in:

    pacman -Syu
    pacman -S vim dialog wpa_supplicant
    wifi-menu
    netctl enable nameofwificonfig
    reboot

## We can now ssh into the Rpi

	ssh root@192.168.1.82
	password: root	

## Now setup the software and all its dependencies

	git clone https://github.com/anthillsocial/suitcase.git
	pacman -S git sox alsa-utils 
    pacman -S aubio python2-cffi python2-numpy
	pacman -S python-cffi python-numpy
    pip install pysoundcard
    cp /usr/lib/python3.4/site-packages/pysoundcard.py /usr/lib/python2.7/site-packages/pysoundcard.py

## And finally create a systemd service so it automatically starts on boot
Paste the follwowing into /
	

# NOTES
Attempted to use pyaudio but kept getting distorted audio.

    git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
    pacman -S libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev


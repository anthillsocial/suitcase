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
    j. Type n, then p for primary, 2 for the second partition on the drive, and then press ENTER twice to accept the default first and last sector.
    k. rite the partition table and exit by typing w.

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

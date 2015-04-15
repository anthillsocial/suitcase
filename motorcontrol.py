#!/bin/python2
import RPi.GPIO as io
#io.setmode(io.BCM)
import sys, tty, termios, time

# This blocks of code defines the three GPIO
# pins used for the stepper motor
#GPIO.setmode(GPIO.BCM) # BOARD
io.setmode(io.BCM) 
motor_enable_pin = 4
motor_direction_pin = 17
motor_step_pin = 24
io.setup(motor_enable_pin, io.OUT)
io.setup(motor_direction_pin, io.OUT)
io.setup(motor_step_pin, io.OUT)


# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# This section of code defines the methods used to determine
# whether the stepper motor needs to spin forward or backwards.
# different directions are acheived by setting the
# direction GPIO pin to true or to false.
# both pins match, the motor will not turn.


def stepper_enable():
    print('enable')
    io.output(motor_enable_pin, True)

def stepper_disable():
    print('disable')
    io.output(motor_enable_pin, False)

def step_once():
    print('step once')
    io.output(motor_step_pin, True)
    time.sleep(.1)
    io.output(motor_step_pin, False)
    time.sleep(.1)

def step_forward():
    io.output(motor_step_pin, True)
    step_once()

def step_reverse():
    io.output(motor_step_pin, False)
    step_once()

# Setting the stepper pins to false so the motors will not move
# until the user presses the first key
io.output(motor_enable_pin, False)
io.output(motor_step_pin, False)

# Instructions for when the user has an interface
print("e: enable")
print("d: disable")
print("f: forwards")
print("r: reverse")
print("g: step forward 10 steps")
print("t: reverse 10 steps")
print("x: exit")

# Infinite loop that will not end until the user presses the
# exit key
while True:
    # Keyboard character retrieval method is called and saved
    # into variable
    char = getch()

    # The stepper will be enabled when the "e" key is pressed
    if(char == "e"):stepper_enable()

    # The stepper will be disabled when the "d" key is pressed
    if(char == "d"):stepper_disable()

    # The "f" key will step the motor forward
    if(char == "f"):step_forward()

    # The "r" key will step the motor in reverse
    if(char == "r"):step_reverse()

    # The "g" key will step the motor 10 steps forwards
    if(char == "g"):
        for x in range(0, 10):
            step_forward()

    # The "t" key will step the motor 10 steps in reverse
    if(char == "t"):
        for x in range(0, 10):
            step_reverse()

    # The "p" key will break the loop and exit the program
    if(char == "x"):
        print("Program Ended")
        break
    
    # The keyboard character variable will be set to blank, ready
    # to save the next key that is pressed
    char = ""

# Program will cease all GPIO activity before terminating
io.cleanup()

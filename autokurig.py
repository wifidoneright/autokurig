#! /usr/bin/python3

try:
    import RPi.GPIO as GPIO
    import time
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
mode = GPIO.getmode()
wLevel = 16
# Setup Pins
GPIO.setup(wLevel, GPIO.OUT)


GPIO.output(wLevel,1) #set water to full

# set channel
# GPIO.setup(channel, GPIO.IN)
# GPIO.setup(channel, GPIO.OUT)
# GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
# read channel
# GPIO.input(channel)
# GPIO.output(channel, state)
# State can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.

# GPIO.setup(wLevel, GPIO.OUT)
# while True:
#     GPIO.output(wLevel,1)
#     time.sleep(1)
#     GPIO.output(wLevel,0)
#     time.sleep(1)


GPIO.cleanup()
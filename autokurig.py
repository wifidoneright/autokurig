#! /usr/bin/python3

try:
    import RPi.GPIO as GPIO
    import time
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
mode = GPIO.getmode()
light = 16
# set channel
# GPIO.setup(channel, GPIO.IN)
# GPIO.setup(channel, GPIO.OUT)
# GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
# read channel
# GPIO.input(channel)
# GPIO.output(channel, state)
# State can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.

GPIO.setup(light, GPIO.OUT)
while True:
    GPIO.output(light,1)
    time.sleep(.5)
    GPIO.output(light,0)


GPIO.cleanup()
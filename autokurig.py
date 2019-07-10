#! /usr/bin/python3

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()
print(mode)
#! /usr/bin/python3

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()
print(mode)
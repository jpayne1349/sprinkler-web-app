# test file to run on the pi while setting up valve control

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # set up for board number, not gpio number
GPIO.setup(37, GPIO.OUT)

on = False
off = True

def commandLineTest():
    while True:
        ans_question = input('0 or 1 : ')
        if( ans_question == '1' ):
            GPIO.output(37, on)
            print('relay True')
        elif( ans_question == 'Exit' ):
            exit()
        else:
            GPIO.output(37, off)
            print('relay False')

commandLineTest()
        
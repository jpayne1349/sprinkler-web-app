# test file to run on the pi while setting up valve control

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # set up for board number, not gpio number
GPIO.setup(37, GPIO.OUT)


def commandLineTest():
    while True:
        ans_question = input('True or False')
        if( ans_question == 'True' ):
            GPIO.output(37, True)
            print('relay True')
        elif( ans_question == 'Exit' ):
            exit()
        else:
            GPIO.output(37, False)
            print('relay False')
        
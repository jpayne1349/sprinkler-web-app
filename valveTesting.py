# test file to run on the pi while setting up valve control

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # set up for board number, not gpio number

board_pins = [3,5,7,8]
GPIO.setup(board_pins, GPIO.OUT, initial=GPIO.HIGH)

on = False
off = True

def commandLineTest():
    while True:
        ans_question = input('Relay # :')
        print('1:', GPIO.input(3), '2:', GPIO.input(4))
        if( ans_question == '1' ):
            if( GPIO.input(3) == 1 ):
                GPIO.output(3, off)
                print('relay one OFF')
            else:
                GPIO.output(3, on)
                print('relay one ON')        
        elif( ans_question == '2' ):
            if( GPIO.input(5) == 1 ):
                GPIO.output(5, off)
                print('relay two OFF')
            else:
                GPIO.output(5, on)
                print('relay two ON')  
        elif( ans_question == '3' ):
            if( GPIO.input(7) == 1 ):
                GPIO.output(7, off)
                print('relay three OFF')
            else:
                GPIO.output(7, on)
                print('relay three ON') 
        elif( ans_question == '4' ):
            if( GPIO.input(8) == 1 ):
                GPIO.output(8, off)
                print('relay four OFF')
            else:
                GPIO.output(8, on)
                print('relay four ON')
        else:
            print('input not valid')



commandLineTest()
        
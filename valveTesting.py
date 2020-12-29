# test file to run on the pi while setting up valve control

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # set up for board number, not gpio number

board_pins = [11,15,13,16]
GPIO.setup(board_pins, GPIO.OUT, initial=GPIO.HIGH)

on = False
off = True

def printStatus():
    print('ONE:', GPIO.input(board_pins[0]), '  TWO:', GPIO.input(board_pins[1]),
                '  THREE:', GPIO.input(board_pins[2]), '  FOUR:', GPIO.input(board_pins[3]))

def commandLineTest():
    while True:
        ans_question = input('Relay # :')
        if( ans_question == '1' ):
            if( GPIO.input(board_pins[0]) == 1 ):
                GPIO.output(board_pins[0], on)
                printStatus()
            else:
                GPIO.output(board_pins[0], off)
                printStatus()      
        elif( ans_question == '2' ):
            if( GPIO.input(board_pins[1]) == 1 ):
                GPIO.output(board_pins[1], on)
                printStatus() 
            else:
                GPIO.output(board_pins[1], off)
                printStatus()   
        elif( ans_question == '3' ):
            if( GPIO.input(board_pins[2]) == 1 ):
                GPIO.output(board_pins[2], on)
                printStatus() 
            else:
                GPIO.output(board_pins[2], off)
                printStatus() 
        elif( ans_question == '4' ):
            if( GPIO.input(board_pins[3]) == 1 ):
                GPIO.output(board_pins[3], on)
                printStatus() 
            else:
                GPIO.output(board_pins[3], off)
                printStatus() 
        else:
            print('input not valid')



commandLineTest()
        
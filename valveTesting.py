# test file to run on the pi while setting up valve control

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # set up for board number, not gpio number

board_pins = [11,13,15,16]
GPIO.setup(board_pins, GPIO.OUT, initial=GPIO.HIGH)

on = False
off = True

def commandLineTest():
    while True:
        ans_question = input('Relay # :')
        print('1:', GPIO.input(board_pins[0]), '2:', GPIO.input(board_pins[1]),
                '3:', GPIO.input(board_pins[2]), '4:', GPIO.input(board_pins[3]))
        if( ans_question == '1' ):
            if( GPIO.input(board_pins[0]) == 1 ):
                GPIO.output(board_pins[0], on)
                print('relay one ON')
            else:
                GPIO.output(board_pins[0], off)
                print('relay one OFF')        
        elif( ans_question == '2' ):
            if( GPIO.input(board_pins[1]) == 1 ):
                GPIO.output(board_pins[1], on)
                print('relay two ON')
            else:
                GPIO.output(board_pins[1], off)
                print('relay two OFF')  
        elif( ans_question == '3' ):
            if( GPIO.input(board_pins[2]) == 1 ):
                GPIO.output(board_pins[2], on)
                print('relay three ON')
            else:
                GPIO.output(board_pins[2], off)
                print('relay three OFF') 
        elif( ans_question == '4' ):
            if( GPIO.input(board_pins[3]) == 1 ):
                GPIO.output(board_pins[3], on)
                print('relay four ON')
            else:
                GPIO.output(board_pins[3], off)
                print('relay four OFF')
        else:
            print('input not valid')



commandLineTest()
        
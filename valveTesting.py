# test file to run on the pi while setting up valve control

# TODO: needs to check every so often that the valves are closed!

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # set up for board number, not gpio number

#                                   as 0,1,2,3
# these in the yard are....  left side (porch area) , side yard (single shooter) , middle yard, right side (farthest) 


board_pins = [11,15,13,16]
GPIO.setup(board_pins, GPIO.OUT, initial=GPIO.HIGH)

# defining them as left , middle, right, and side

left = board_pins[0]
middle = board_pins[2]
right = board_pins[3]
side = board_pins[1]

on = False
off = True

def interpret(value):
    if value == 0:
        return 'ON'
    elif value == 1:
        return 'OFF'

def printStatus():
    print('ONE:', interpret(GPIO.input(board_pins[0])), '  TWO:', interpret(GPIO.input(board_pins[1])),
                '  THREE:', interpret(GPIO.input(board_pins[2])), '  FOUR:', interpret(GPIO.input(board_pins[3])))


# run for manual control via command line
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
        
import RPi.GPIO as GPIO
import time
import telegram_send
import os

from flask import current_app

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

# helpful for the setting of the pins, False = Ground = RelayON
on = False
off = True

def run(minutes):
    if type(minutes) != int:
        minutes = int(minutes)
    
    telegram_send.send(messages=[f'Running backyard sprinklers. Input time = {minutes} minutes.'])
    on_time = minutes * 60
     
    # every time, only run side yard for 1 minute at beginning and 1 minute at end...
    
    # side on for 60
    GPIO.output(side, on)
    telegram_send.send(messages=['Sideyard on'])
    time.sleep(120)

    # turn left on before stopping
    GPIO.output(left, on)
    telegram_send.send(messages=['Porchside on'])

    # stop side after 1 second
    time.sleep(1)
    GPIO.output(side, off)
    telegram_send.send(messages=['Sideyard off'])

    # leave left on for alloted time
    time.sleep(on_time)

    # turn the middle on
    GPIO.output(middle, on)
    telegram_send.send(messages=['Middle on'])
    # wait 1 second and turn the left off
    time.sleep(1)
    GPIO.output(left, off)
    telegram_send.send(messages=['Porchside off'])

    # leave middle on for alloted time
    time.sleep(on_time)

    # turn the right on
    GPIO.output(right, on)
    telegram_send.send(messages=['Farside on'])
    # wait 1 second and turn the middle off
    time.sleep(1)
    GPIO.output(middle, off)
    telegram_send.send(messages=['Middle off'])

    #leave right on for alloted time
    time.sleep(on_time)

    #turn the side on
    GPIO.output(side, on)
    telegram_send.send(messages=['Sideyard on'])

    # wait 1 second and turn the right off
    time.sleep(1)
    GPIO.output(right, off)
    telegram_send.send(messages=['Farside off'])

    # leave the side on
    time.sleep(120)
    # and turn it off
    GPIO.output(side, off)
    telegram_send.send(messages=['Sideyard off'])

    # for now just print their status...
    # and send message with values..
    return printStatus()

def stop():
    telegram_send.send(messages=[f'Sprinkler script stopped via homekit'])
    #time.sleep(1)
    GPIO.output(side, off)
    #time.sleep(1)
    GPIO.output(left, off)
    #time.sleep(1)
    GPIO.output(middle, off)
    #time.sleep(1)
    GPIO.output(right, off)

    printStatus()

def interpret(value):
    if value == 0:
        return 'ON'
    elif value == 1:
        return 'OFF'

def getStatus():
    l = GPIO.input(left)
    m = GPIO.input(middle)
    r = GPIO.input(right)
    s = GPIO.input(side)
    if 0 in (l, m, r, s):
        return '1'
    else:
        return '0'
    

def printStatus():
    telegram_send.send(messages=[f'Left: {interpret(GPIO.input(left))}  Middle: {interpret(GPIO.input(middle))} Right: {interpret(GPIO.input(right))} Side: {interpret(GPIO.input(side))}'])

    print('Left:', interpret(GPIO.input(left)), '  Middle:', interpret(GPIO.input(middle)),
                '  Right:', interpret(GPIO.input(right)), '  Side:', interpret(GPIO.input(side)))

try:
    run(5)
    
except Exception as error:
    traceback_list = traceback.format_exception(
        etype=type(error), value=error, tb=error.__traceback__)
    print()
    traceback_string = "".join(traceback_list)
    print(traceback_string)

    telegram_send.send(messages=['Job failed! Traceback of error: ', traceback_string])

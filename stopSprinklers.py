import RPi.GPIO as GPIO
import time
import telegram_send
import os

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


# task to be run as a cronjob, notifying of start, stop, and status
def run(minutes):
    if type(minutes) != int:
        minutes = int(minutes)
    
    telegram_send.send(messages=[f'Running backyard sprinklers. Input time = {minutes} minutes.'])
    on_time = minutes * 60
     
    # every time, only run side yard for 1 minute at beginning and 1 minute at end...
    GPIO.output(side, on)
    telegram_send.send(messages=['Sideyard on'])
    time.sleep(60)
    GPIO.output(side, off)
    telegram_send.send(messages=['Sideyard off'])

    GPIO.output(left, on)
    telegram_send.send(messages=['Porchside on'])
    time.sleep(on_time)
    GPIO.output(left, off)
    telegram_send.send(messages=['Porchside off'])

    GPIO.output(middle, on)
    telegram_send.send(messages=['Middle on'])
    time.sleep(on_time)
    GPIO.output(middle, off)
    telegram_send.send(messages=['Middle off'])

    GPIO.output(right, on)
    telegram_send.send(messages=['Farside on'])
    time.sleep(on_time)
    GPIO.output(right, off)
    telegram_send.send(messages=['Farside off'])

    GPIO.output(side, on)
    telegram_send.send(messages=['Sideyard on'])
    time.sleep(60)
    GPIO.output(side, off)
    telegram_send.send(messages=['Sideyard off'])

    # for now just print their status...
    return printStatus()

# running in this script to ensure valves are closed.

def stop():
    telegram_send.send(messages=[f'Sprinkler script stopped via homekit'])
    time.sleep(1)
    GPIO.output(side, off)
    time.sleep(1)
    GPIO.output(left, off)
    time.sleep(1)
    GPIO.output(middle, off)
    time.sleep(1)
    GPIO.output(right, off)
    
    return printStatus()

def interpret(value):
    if value == 0:
        return 'ON'
    elif value == 1:
        return 'OFF'

def printStatus():
    telegram_send.send(messages=[f'Left: {interpret(GPIO.input(left))}  Middle: {interpret(GPIO.input(middle))} Right: {interpret(GPIO.input(right))} Side: {interpret(GPIO.input(side))}'])

    print('Left:', interpret(GPIO.input(left)), '  Middle:', interpret(GPIO.input(middle)),
                '  Right:', interpret(GPIO.input(right)), '  Side:', interpret(GPIO.input(side)))

try:
    stop()
    if os.path.exists("status.flag"):
        os.remove("status.flag")
    else:
        telegram_send.send(messages=['No status flag found for removal'])
        raise Exception
    exit()
    
except Exception as error:
    traceback_list = traceback.format_exception(
        etype=type(error), value=error, tb=error.__traceback__)
    print()
    traceback_string = "".join(traceback_list)
    print(traceback_string)

    telegram_send.send(messages=['Job failed! Traceback of error: ', traceback_string])

import RPi.GPIO as GPIO
import time
import telegram_send

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
        return print('Input not a number')
    
    on_time = minutes * 60

    # every time, only run side yard for 1 minute at beginning and 1 minute at end...
    GPIO.output(side, on)
    time.sleep(60)
    GPIO.output(side, off)

    GPIO.output(left, on)
    time.sleep(on_time)
    GPIO.output(left, off)

    GPIO.output(middle, on)
    time.sleep(on_time)
    GPIO.output(middle, off)

    GPIO.output(right, on)
    time.sleep(on_time)
    GPIO.output(right, off)

    # for now just print their status...
    return printStatus()


def interpret(value):
    if value == 0:
        return 'ON'
    elif value == 1:
        return 'OFF'

def printStatus():
    print('Left:', interpret(GPIO.input(left)), '  Middle:', interpret(GPIO.input(middle)),
                '  Right:', interpret(GPIO.input(right)), '  Side:', interpret(GPIO.input(side)))


run(input('How many minutes? '))
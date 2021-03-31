import RPi.GPIO as GPIO
import telegram_send
import os
import asyncio

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


async def run_sprinklers(minutes):
    on_time = minutes * 60


    # turn the valve on, and then do the await?
    GPIO.output(side, on)
    telegram_send.send(messages=['Sideyard on'])
    await asyncio.sleep(60)
    GPIO.output(side, off)
    telegram_send.send(messages=['Sideyard off'])

    GPIO.output(left, on)
    telegram_send.send(messages=['Porchside on'])
    await asyncio.sleep(on_time)
    GPIO.output(left, off)
    telegram_send.send(messages=['Porchside off'])

    GPIO.output(middle, on)
    telegram_send.send(messages=['Middle on'])
    await asyncio.sleep(on_time)
    GPIO.output(middle, off)
    telegram_send.send(messages=['Middle off'])

    GPIO.output(right, on)
    telegram_send.send(messages=['Farside on'])
    await asyncio.sleep(on_time)
    GPIO.output(right, off)
    telegram_send.send(messages=['Farside off'])

    GPIO.output(side, on)
    telegram_send.send(messages=['Sideyard on'])
    await asyncio.sleep(60)
    GPIO.output(side, off)
    telegram_send.send(messages=['Sideyard off'])
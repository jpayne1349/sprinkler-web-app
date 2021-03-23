#!/usr/bin/env bash


# ampersand says to run in subshell async

cd /home/homebridge/sprinklers

python3 runSprinklers.py &

touch status.flag
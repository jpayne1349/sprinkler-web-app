#!/usr/bin/env bash


# need to kill original script and run a stopping script.

pkill -f runSprinklers.py

python3 stopSprinklers.py &


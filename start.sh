#!/usr/bin/env bash


# ampersand says to run in subshell async

python3 runSprinklers.py &

touch status.flag
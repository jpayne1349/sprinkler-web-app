#!/usr/bin/env bash


# ampersand says to run in subshell async

cd /home/jpayne/Desktop/github/sprinklers

python3 runSprinklers.py &

touch status.flag
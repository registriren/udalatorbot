#!/bin/sh
python3 udalatorbot.py >> log.txt 2>&1 & echo $! >> log.pid

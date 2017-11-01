# Raspberry Pi normie power button
# script uses a button on pin 5 held for 3 seconds to halt the CPU,
# The advantage of pin 5 is that the bootloader can also use this button to wake the CPU.

import RPi.GPIO as GPIO
import os
import time

btn_channel = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(btn_channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(True):
    GPIO.wait_for_edge(btn_channel, GPIO.FALLING)
    time.sleep(3)
    if GPIO.input(btn_channel) == GPIO.LOW:
      os.system("sudo shutdown -h now")

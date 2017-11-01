# Raspberry Pi normie power button
# script uses a button on pin 5 held for 2 seconds to halt the CPU,
# then the bootloader will wake from halt when the button is pressed.
# Also I wrote this so.. this script is likely junk

import RPi.GPIO as GPIO
import os
import time

btn_channel = 5
led_channel = 10

GPIO.setmode(GPIO.BOARD)

GPIO.setup(btn_channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_channel, GPIO.OUT)

GPIO.output(led_channel, GPIO.HIGH)

while(True):
    GPIO.wait_for_edge(btn_channel, GPIO.FALLING)
    falling_edge_time = time.time()
    
    GPIO.wait_for_edge(btn_channel, GPIO.RISING)
    rising_edge_time = time.time()
    
    if rising_edge_time - falling_edge_time > 2:
      GPIO.output(led_channel, GPIO.LOW)
      os.system("sudo shutdown -h now")

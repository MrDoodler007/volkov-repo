import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(8)]

def dec2dac(dec):
    GPIO.output(dac,dec2bin(dec))

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
    while True:
        for i in range (255):
            dec2dac(i)
            time.sleep(0.03)
        for i in range (255):
            dec2dac(255-i)
            time.sleep(0.03)
            
        
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
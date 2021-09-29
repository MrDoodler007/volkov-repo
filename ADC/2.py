import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
maxV = 3.3

def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(8)]

def dec2dac(dec):
    GPIO.output(dac,dec2bin(dec))

def adc():
    ans = 0
    for i in range(8):
        ans = ans + 2**(7-i)
        dec2dac(ans)
        time.sleep(0.001)
        if GPIO.input(4) == 0:
            ans = ans - 2**(7-i)
    print("Value is {:^3} Voltage is {:.2f}".format(ans, ans/255*3.3))
    
    # for i in range(255):
    #     dec2dac(i)
    #     time.sleep(0.001)
    #     if GPIO.input(4) == 0:
    #         print("Value is {} Voltage is {}".format(i, i/255*3.3))
    #         break

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(17, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(4, GPIO.IN)

try:
    while True:
        adc()
        
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
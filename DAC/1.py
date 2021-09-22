import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
maxV = 3.3

def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(8)]

def dec2dac(dec):
    GPIO.output(dac,dec2bin(dec))

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
    while True:
        inp = input("Enter a value between 0 and 255 (Ctrl + C for exit) >> ")

        if inp.isdigit():
            value = int(inp)
            print("Value = {:3} = {}, Voltage = {:.2f}".format(value, dec2bin(value), value*3.3/256))
        elif not inp.isdigit():
            print("Achtung! Enter a positive integer!")
            continue

        if value > 255:
            print("Achtung! Value is out of range (0..255)")
            continue
        else:
            dec2dac(value)
        
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
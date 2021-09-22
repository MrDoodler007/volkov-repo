import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, 0)
p = GPIO.PWM(22, 1000)
try:
    
    p.start(0)
    while True:
        dc = input("Enter dc between 0 and 100 >> ")
        if dc.isdigit():
            dc = int(dc)
            if dc < 0 or dc > 100:
                print("Achtung! Value is out of range!")
                continue
            else:
                p.ChangeDutyCycle(dc)

        else:
            print("Achtung! Enter correct value!")

finally:
    p.stop()
    GPIO.output(22, GPIO.LOW)
    GPIO.cleanup()
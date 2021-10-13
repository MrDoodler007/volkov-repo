import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
value_list = []

def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(8)]

def dec2leds(dec):
    GPIO.output(leds,dec2bin(dec))

def adc():
    ans = 0
    for i in range(8):
        ans = ans + 2**(7-i)
        dec2leds(ans)
        time.sleep(0.001)
        if GPIO.input(4) == 0:
            ans = ans - 2**(7-i)
    return ans


GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

try:
    begin = time.time()
    GPIO.output(17, 1)
    print("Конденсатор заряжается")
    while adc() < 250:
        value_list.append(adc())
        dec2leds(value_list[-1])
        print(value_list[-1])
    
    GPIO.output(17, GPIO.LOW)
    print("Конденсатор разряжается")

    #while adc() > 1:
    for i in range(10):
        value_list.append(adc())
        dec2leds(value_list[-1])
        print(value_list[-1])

    duration = time.time() - begin
    print("Duration = {:.3f} sec".format(duration))
    print("Sampling frequency = {:.1f} Hz".format(len(value_list)/duration))
    print("Period = {:.3f} sec".format(1/(len(value_list)/duration)))
    print("Voltage step = {:.3f} V".format(3.3/255))

    plt.plot(value_list)
    plt.show()

    value_list_str = [str(item) for item in value_list]

    with open("data.txt", "w") as data:
        data.write("\n".join(value_list_str))
    with open("settings.txt", "w") as settings:
        settings.write("Duration = " + "".join(str(duration)) + " sec" + "\n")
        settings.write("Sampling frequency = " + "".join(str(len(value_list)/duration)) + " Hz" + "\n")
        settings.write("Period = " + "".join(str(1/(len(value_list)/duration))) + " sec" + "\n")
        settings.write("Voltage step = " + "".join(str(3.3/255)) + " V")
        
finally:
    GPIO.output(leds + [17], GPIO.LOW)
    GPIO.cleanup()
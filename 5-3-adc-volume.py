import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
bits = 8
levels = 2 ** 8
maxV = 3.3
trM = 17
comp = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(trM, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def d2b(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(dac, d2b(k))
        time.sleep(0.007)
        if GPIO.input(comp) == 0:
            k-=2**i 
    return(k)


def get_led(volt):
    ans = []
    k = 0.8/8
    for i in range(8):
        if i * k > volt:
            ans.append(0)
        else:
            ans.append(1)
    return ans 


try:
    while True:
        a=adc()
        volt = round(3.3*a/256, 3)
        t = get_led(volt)
        GPIO.output(leds, t)
        if a!=0:
            print(a, volt)

except KeyboardInterrupt:
    print(1)
else:
    print("NO")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup(dac)


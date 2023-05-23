import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = 8
levels = 2 ** 8
maxV = 3.3
trM = 17
comp = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(trM, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def d2b(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(dac, d2b(k))
        time.sleep(0.07)
        if GPIO.input(comp)==0:
            k-=2**i 
    return(k)
try:
    while True:
        a=adc()
        volt = round(3.3*a/256, 3)
        if a!=0:
            print(a, volt)

except KeyboardInterrupt:
    print(1)
else:
    print("NO")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)


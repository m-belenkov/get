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


def d2b(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(bits)]


def n2d(val):
    signal = d2b(val)
    GPIO.output(dac, signal)
    return signal


try:
    while True:
        for value in range(256):
            time.sleep(0.007)
            signal = n2d(value)
            valtage = value / levels * maxV
            valtage = round(valtage, 3)
            compvalue = GPIO.input(comp)
            if compvalue == 0:
                print(value, valtage)
                break

except KeyboardInterrupt:
    print(1)
else:
    print("NO")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)



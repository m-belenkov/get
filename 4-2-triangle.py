import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    T = input()
    while T != "q":
        T = int(T)
        for i in range(256):
            line = dec2bin(i)
            GPIO.output(dac, line)
            time.sleep(T/512)
        for i in range(255, -1, -1):
            line = dec2bin(i)
            GPIO.output(dac, line)
            time.sleep(T/512)
        T = input()
except Exception:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()

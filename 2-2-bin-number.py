import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0 for i in range(8)]
a = bin(int(input()))[2:]

while len(a) != 8:
    a = "0" + a

number = [int(a[i]) for i in range(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)

time.sleep(10)
GPIO.output(dac, GPIO.LOW)
GPIO.cleanup()
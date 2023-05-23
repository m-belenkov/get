import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)
for _ in range(1):
    for i in leds:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(i, GPIO.LOW)

GPIO.output(leds, GPIO.LOW)
GPIO.cleanup()

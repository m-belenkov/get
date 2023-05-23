import RPi.GPIO as GPIO

aux = [22, 23, 27, 18, 15, 14, 3, 2]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)
p.start(0)

try:
    while True:
        duty_cycle = int(input())
        p.start(duty_cycle)
        print(duty_cycle * 3.3 / 100)
finally:
    GPIO.cleanup()

import RPi.GPIO as GPIO


def get_2(a):
    t = 3.3 / 256
    b = bin(a)[2::]

    while len(b) < 8:
        b = "0" + b

    volt = t * a

    return b, volt

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(dac, GPIO.OUT)


try:
    a = input()
    while a != "q":
        if int(a) < 256:
            line, v = get_2(int(a))
            line = [int(line[i]) for i in range(8)]
            GPIO.output(dac, line)
            print(v)
        else:
            print("Введите число от 0 до 255 или q для выхода")
        a = input()
    else:
        GPIO.output(dac, GPIO.LOW)
        GPIO.cleanup()
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()



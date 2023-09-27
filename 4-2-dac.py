import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [6, 12, 5, 0, 1, 7, 11, 8][::-1]
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, 0)


def to_bin(num):
    return [int(i) for i in bin(int(num))[2:].zfill(8)]


def value(num):
    return ('{:.4f}'.format((int(num) / 2**8) * 3.3))


t = float(input("Период "))
try:
    c = 0
    while True:
        GPIO.output(dac, 0)
        time.sleep(1)
        d = t / 510
        for i in range(0, 256):
            print(value(i))
            GPIO.output(dac, to_bin(i))
            time.sleep(d)
        for i in range(254, 0, -1):
            print(value(i))
            GPIO.output(dac, to_bin(i))
            time.sleep(d)
        c += 1
        if c == 1:
            break
    GPIO.output(dac, 0)
    print(value(0))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

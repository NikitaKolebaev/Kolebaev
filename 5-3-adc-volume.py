import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6][::-1]
leds = [9, 10, 22, 27, 17, 4, 3, 2]
light = [0] * 8
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT, initial = 0)


def to_bin(num):
    return [int(i) for i in bin(int(num))[2:].zfill(8)]


def adc():
    tar = [0] * 8
    light = [0] * 8
    for i in range(0, len(tar)):
        tar[i] = 1
        GPIO.output(dac, tar[::-1])
        time.sleep(0.002)
        if GPIO.input(comp) == 1:
            tar[i] = 0
    dig = sum([2**(7-j) * tar[j] for j in range(0, len(tar))])
    volume = math.ceil((dig / 255) * 8)
    for i in range(0, volume):
        light[i] = 1
    GPIO.output(leds, light)
    return dig
        

def value(num):
    return ('{:.4f}'.format((int(num) / 2**8) * 3.3))


try:
    while True:
        dig = adc()
        print(dig, value(dig))
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()
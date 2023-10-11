import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [6, 12, 5, 0, 1, 7, 11, 8][::-1]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(dac + leds, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.output(dac + leds + [24], 0)
p = GPIO.PWM(9, 0.5)
rc = GPIO.PWM(24, 0.5)
rc.start(0)
p.start(0)

def value_V(num):
    return ('{:.4f}'.format(int(num) / 100 * 3.3))


def value_bin(num):
    return int(num / 100 * 255)


def to_bin(decimal):
    return [int(i) for i in bin(decimal)[2:].zfill(8)]


try:
    while True:
        duty_cycle = int(input("Введите duty cycle: "))
        p.ChangeDutyCycle(duty_cycle)
        rc.ChangeDutyCycle(duty_cycle)
        print(value_V(duty_cycle))
        GPIO.output(dac, to_bin(value_bin(duty_cycle)))
finally:
    GPIO.output(dac + leds, 0)
    p.stop()
    rc.stop()
    GPIO.cleanup()



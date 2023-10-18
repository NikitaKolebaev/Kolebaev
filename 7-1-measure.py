import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
dac = [6, 12, 5, 0, 1, 7, 11, 8][::-1]
leds = [9, 10, 22, 27, 17, 4, 3, 2][::-1]
data = []
troyka = 13
comp = 14
accuracy = 0.013
levels = 2**8
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac + leds, GPIO.OUT, initial = 0)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)


def adc():
    tar = [0] * 8
    for i in range(0, 8):
        tar[i] = 1
        GPIO.output(dac, tar)
        time.sleep(0.003)
        if GPIO.input(comp) == 1:
            tar[i] = 0
    return sum([2**(7 - j) * tar[j] for j in range(0, len(tar))])


def voltage(num):
    return float('{:.4f}'.format(int(num) / 255 * 3.3))


def to_bin(num):
    return [int(i) for i in bin(int(num))[2:].zfill(8)]


def let_there_be_light(values):
    GPIO.output(leds, values)


try:
    while voltage(adc()) >= accuracy:
        pass 
    GPIO.output(troyka, 1)
    print("Началась зарядка...")
    flag = False
    count = 0
    while adc() <= 206:
        if flag is False:
            t_start = time.time()
            flag = True
        cur = adc()
        data.append(voltage(cur))
        # print(cur)
        let_there_be_light(to_bin(cur))
        count += 1
    GPIO.output(troyka, 0)
    t_middle = time.time()
    print("Началась разрядка...")
    while adc() >= 193:
        cur = adc()
        data.append(voltage(cur))
        let_there_be_light(to_bin(cur))
        # print(cur)
        count += 1
    t_end = time.time()
    overall_time = t_end - t_start
    nu = str('{:.4f}'.format(1 / overall_time * count))
    T = str('{:.4f}'.format(t_middle - t_start))
    overall_time = str('{:.4f}'.format(overall_time))
    print("Эксперимент окончен")
    plt.plot(data)
    plt.show()
    data = map(str, data)
    with open('/home/b03-302/Desktop/Scripts/Kolebaev/data.txt', 'w') as file:
        file.write('\n'.join(data))
    file.close()
    with open('/home/b03-302/Desktop/Scripts/Kolebaev/settings.txt', 'w') as file:
        file.write("Время: " + overall_time + "c" + "\n" + "Период: " + T + "c" + '\n' + "Частота дискретизации: " + nu + "Гц" + '\n' + "Шаг квантования: 0.0129 В ")
    file.close()
finally:
    GPIO.output(leds + dac + [troyka], 0)
    GPIO.cleanup()
import jetFunctions as jet
import time
import RPi.GPIO as GPIO
from array import*
import json


step = 2
kol = 500
try:
    mes = []
    jet.initSpiAdc()
    jet.initStepMotorGpio()
    jet.stepForward(500)
    for i in range(kol):
        mes.append(jet.getAdc())
        jet.stepBackward(step)
        time.sleep(0.1)
    jet.stepForward(500)


finally:
    jet.deinitStepMotorGpio()
    jet.deinitSpiAdc()
    a = sum(mes)/len(mes)       
    print("average:", a)
    print(mes)
    mes_str = [str(i) for i in mes]
    with open('00.txt', 'w') as file:
        file.write("\n".join(mes_str))


 






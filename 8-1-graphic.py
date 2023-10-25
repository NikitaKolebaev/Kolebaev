import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

with open('data.txt') as file:
    data_v = np.array(list(map(float, file.read().split('\n'))))
with open('settings.txt') as file:
    data = [float(line) for line in file.read().split('\n')]
for i in range(0, len(data)):
    data[i] = float('{:.4f}'.format(data[i]))
dt = data[0] / len(data_v)
data_t = np.arange(0, data[0], dt)
max_t = data_t[data_v.argmax()]
t_recharge = data_t[len(data_t) - 1] - max_t

fig, ax = plt.subplots(figsize = (16, 9))
ax.plot(data_t, data_v, color='blue', label='V(t)')
for i in range(0, len(data_v), 5):
    ax.scatter(data_t[i], data_v[i], marker='o', color='blue')

ax.set_title('График зав-ти напряжения на конденсаторе от времени', loc='center')
ax.xaxis.grid(True, which='minor', color='#D3D3D3')
ax.xaxis.grid(True, which='major', color='#696969')
# ax.grid(False, which='both', color='black')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(0.2))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
plt.xlabel('Время, с')

ax.yaxis.grid(True, which='minor', color='#D3D3D3')
ax.yaxis.grid(True, which='major', color='#696969')
# ax.grid(False, which='both', color='black')
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.4f}'))
plt.ylabel('Напряжение, В')
plt.text(6.5, 1.5, 'Время зарядки: ' + '{:.4f}'.format(max_t) + ' c')
plt.text(6.5, 1.4, 'Время разрядки: ' + '{:.4f}'.format(t_recharge) + ' c')
ax.legend()
fig.savefig('rc_graphic.svg')
plt.show()
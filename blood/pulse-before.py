import matplotlib.pyplot as plt
import numpy as np

with open('data_t.txt', 'r') as file:
    data_t = list(map(float, file.read().split('\n')))
    file.close()
with open('data_p.txt', 'r') as file:
    data_p = list(map(float, file.read().split('\n')))
    file.close()
with open('app1.txt', 'r') as file:
    k = float(file.readline())
    b = float(file.readline())
    file.close()

for i in range(0, len(data_p)):
    data_p[i] = data_p[i] - (k * data_t[i] + b)

fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(data_t, data_p, color='blue', linewidth=1, label='Пульс - 66 уд/мин')
ax.set_xlim(7.5, 18.5)
ax.set_ylim(-2.5, 2.5)

ax.set_xlabel('Время (t), c')
ax.set_ylabel('Давление (p), мм.рт.ст.')

ax.minorticks_on()
ax.grid(which='minor', color='lightgrey', linestyle='--')
ax.grid(which='major', color='grey', linestyle='-')
ax.grid(True, which='both')

title_text = ('Зависимость значения артериального давления от времени '
              '(с исключенной линейной частью) в спокойном состоянии')
ax.set_title(title_text, wrap=True)
ax.legend()
plt.savefig('pulse_in_rest.png', format='png')
plt.show()

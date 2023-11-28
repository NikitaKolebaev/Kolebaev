import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
with open('coeff.txt', 'r') as file:
    k, b = list(map(float, file.read().split('\n')))
    file.close()

data_y = np.loadtxt('after.txt')
data_x = []
dt = 50 / np.size(data_y)
time = dt
# print(dt)
data_y = float(k) * data_y + float(b)
flag_s = False
flag_d = False
sist = 0
dias = 0
for i in range(0, np.size(data_y)):
    data_x.append(time)
    time += dt
    if time >= 7 and flag_s is False:
        sist = i
        flag_s = True
    if time >= 17 and flag_d is False:
        dias = i
        flag_d = True
    if time >= 25:
        break
data_x = np.array(data_x)
data_limited = [data_y[i] for i in range(0, len(data_x))]

fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(data_x, data_limited, color='green', linewidth=2, label='p(t)')
ax.scatter(data_x[sist], data_y[sist], color='red', marker='o')
ax.scatter(data_x[dias], data_y[dias], color='red', marker='o')
ax.set_xlim(0, 25)
ax.set_ylim(60, max(data_limited) + 10)

ax.set_xlabel('Время (t), c')
ax.set_ylabel('Давление (p), мм.рт.ст.')

ax.minorticks_on()
ax.grid(which='minor', color='lightgrey', linestyle='--')
ax.grid(which='major', color='grey', linestyle='-')
ax.grid(True, which='both')

title_text = 'Зависимость значения артериального давления от времени после нагрузки'
text_sist_x = data_x[sist]
text_sist_y = data_y[sist]
text_dias_x = data_x[dias]
text_dias_y = data_y[dias]
plt.text(text_sist_x + 0.4, text_sist_y, 'Систола', fontsize=7)
plt.text(text_dias_x + 0.4, text_dias_y, 'Диастола', fontsize=7)
plt.text(text_sist_x + 11, text_sist_y + 10, 'Давление: '
         + str(int(data_y[sist])) + '/' + str(int(data_y[dias])), fontsize=10)
ax.set_title(title_text, wrap=True)
ax.legend()
plt.savefig('after_corrected.png', format='png')
plt.show()

data_x = [str(i) for i in list(data_x)]
data_limited = [str(i) for i in list(data_limited)]
with open('data_p_1.txt', 'w') as file:
    file.write('\n'.join(data_limited))
    file.close()
with open('data_t_1.txt', 'w') as file:
    file.write('\n'.join(data_x))
    file.close()
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

data_x = []
for i in range(40, 161, 40):
    temp = np.loadtxt(str(i) + '.txt')
    data_x.append(round(sum(temp) / temp.size, 1))
data_y = np.array([40, 80, 120, 160])
data_x = np.array(data_x)

coeffs = np.polyfit(data_x, data_y, 1)
k, b = coeffs
# path = Path('D', 'Учеба', 'Программирование', 'Python', 'Labs_1st_sem', 'pl+kb+vr', 'coeff.txt')
# print(path)
with open('coeff.txt', 'w') as file:
    file.write(str(k)+'\n'+str(b))
    file.close()
x_line = np.linspace(0, max(data_x), 1800)
y_line = k * x_line + b
fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(data_x, data_y, color='green', marker='o', label='Калибровочные значения')
ax.plot(x_line, y_line, color='blue', linewidth=2, label='Аппроксимация')
ax.set_xlim(0, max(data_x) + 100)
ax.set_ylim(0, max(data_y) + 40)

ax.set_xlabel('Отсчёты АЦП (N)')
ax.set_ylabel('Давление (p), мм.рт.ст.')

ax.minorticks_on()
ax.grid(which='minor', color='lightgrey', linestyle='--')
ax.grid(which='major', color='grey', linestyle='-')
ax.grid(True, which='both')

text_1 = '{:.4f}'.format(k)
text_2 = '{:.4f}'.format(b)
plt.text(950, 50, 'Коэффициент угла наклона: '+ text_1, fontsize=8)
plt.text(950, 42, 'Пересечение с осью OY: '+ text_2, fontsize=8)

title_text = 'Калибровочный график давления от отсчётов АЦП'
ax.set_title(title_text, wrap=True)
ax.legend()
plt.savefig('calibration.png', format='png')
plt.show()

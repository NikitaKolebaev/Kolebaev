from matplotlib import pyplot as plt
import numpy as np



X = [0, 10, 20, 30, 40, 50, 60, 70]
Y = [3.11, 3.17, 3.96, 4.35, 4.37, 4.81, 6.03, 6.17]
fig, ax = plt.subplots(figsize=(8, 10))
ax.plot(X, Y, label='расход Q (0-70 мм)', color='black')
ax.scatter(X, Y, color='red', marker='x')

ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which='minor', linestyle = ':')

ax.set_xlabel("Расстояние от трубки Пито до сопла, мм")
ax.set_ylabel("Расход, г/с")

ax.legend()
plt.show()
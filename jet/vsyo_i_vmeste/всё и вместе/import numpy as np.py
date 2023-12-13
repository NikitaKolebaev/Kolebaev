import numpy as np
import matplotlib.pyplot as plt

# Входные данные - координаты точек
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([3.11, 3.17, 3.96, 4.35, 4.37, 4.81, 6.03, 6.17])

# Построение аппроксимирующей прямой
coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
x_approx = np.linspace(min(x), max(x), 100)
y_approx = polynomial(x_approx)

# Вывод значений коэффициентов аппроксимирующей прямой
print("Коэффициенты аппроксимирующей прямой:")
print("a =", coefficients[0])
print("b =", coefficients[1])

# Построение графика
plt.scatter(x, y, color='red', marker='x', label='Значения')
plt.plot(x_approx, y_approx, color='black', label='Аппроксимирующая прямая')
plt.xlabel('Расстояние от сопла, см ')
plt.ylabel('Расход, г/с ')
plt.legend()
plt.grid(which='major', linewidth = 0.9999)
plt.grid(which='minor', linestyle = '-')
plt.grid(True)
plt.savefig('График зависимости расхода от расстояния до сопла.png')
plt.show()

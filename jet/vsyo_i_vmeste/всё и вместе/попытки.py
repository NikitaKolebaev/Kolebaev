import numpy as np
import matplotlib.pyplot as plt
y1 = np.array([3.7, 146.1])
x1 = np.array([733.2, 1481.43]) 
t1 = np.polyfit(x1, y1, 1)
f1 = np.poly1d(t1)
print(f1)

fig, ax = plt.subplots()
ax.minorticks_on()
ax.grid(which='minor',color='gray',linestyle=':')
ax.plot(x1, y1, color='black', linestyle='-', linewidth= 1, marker='x', markersize=3, markerfacecolor='white', markeredgewidth=1.5, markeredgecolor='red', label = f1)
ax.set_ylabel('Давление, Па')
ax.set_xlabel('Отсчеты АЦП')
ax.grid(True, color='lightgray', linestyle='-')
ax.legend()
plt.show()
fig.savefig('1.png')
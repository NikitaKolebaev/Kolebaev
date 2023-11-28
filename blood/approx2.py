import matplotlib.pyplot as plt
import numpy as np

data_t = []
data_p = []
with open('data_t_1.txt', 'r') as file:
    temp = list(map(float, file.read().split('\n')))
    for i in range(int(0.42 * len(temp)), len(temp), 10):
        data_t.append(temp[i])
with open('data_p_1.txt', 'r') as file:
    temp = list(map(float, file.read().split('\n')))
    for i in range(int(0.42 * len(temp)), len(temp), 10):
        data_p.append(temp[i])

data_t = np.array(data_t)
data_p = np.array(data_p)

coeffs = np.polyfit(data_t, data_p, 1)
k, b = coeffs
print(k, b)
with open('app2.txt', 'w') as file:
    file.write(str(k)+'\n'+str(b))
    file.close()

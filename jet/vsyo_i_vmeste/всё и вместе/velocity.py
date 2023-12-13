from matplotlib import pyplot as plt
import numpy as np

P_k = 3.7
P_0 = 1189.756/P_k  #1189
dr = 1

ro = 1.34
deltr = 0.45
count = int(24/0.45)+1
pressure_00 = []

with open("00.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_00.append(p)

X_00 = [1.5 + i*0.45 for i in range(len(pressure_00))]
Y_00 = [(2.4*pressure_00[i])**0.5 for i in range(len(pressure_00))]
consumption_00 = 0
for i in range(count):
    # consumption_00 += 1.2*3.14*0.00045*(abs(-0.024 + i*0.00045)*((1.7*pressure_00[i])**0.5) +
    #                               abs(-0.024 + (i+1)*0.00045)*((1.7*pressure_00[i + 1])**0.5))
    consumption_00 += (2*pressure_00[i]*ro)**0.5*np.pi*(2*abs(X_00[i]*deltr) - deltr**2)
pressure_10 = []
with open("10.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_10.append(p)

pressure_10.pop(0)
X_10 = [-5 + i*0.45 for i in range(len(pressure_10))]
Y_10 = [(2.4*pressure_10[i])**0.5 for i in range(len(pressure_10))]
consumption_10 = 0
for i in range(count):
    # consumption_10 += p*np.pi*dr*(i*dr*((1.7*pressure_10[i])**0.5) +
    #                               (i + 1)*dr*((1.7*pressure_10[i + 1])**0.5))
    consumption_10 += (2*pressure_10[i]*ro)**0.5*np.pi*(2*abs(X_10[i]*deltr) - deltr**2)

pressure_20 = []
with open("20.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_20.append(p)

X_20 = [- 5 + i*0.45 for i in range(len(pressure_20))]
Y_20 = [(2.4*pressure_20[i])**0.5 for i in range(len(pressure_20))]
consumption_20 = 0
for i in range(count):
    # consumption_20 += p*np.pi*dr*(i*dr*((1.7*pressure_20[i])**0.5) +
    #                               (i + 1)*dr*((1.7*pressure_20[i + 1])**0.5))
    consumption_20 += (2*pressure_20[i]*ro)**0.5*np.pi*(2*abs(X_20[i]*deltr) - deltr**2)

pressure_30 = []
with open("30.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_30.append(p)
pressure_30.pop(0)
X_30 = [-2 + i*0.45 for i in range(len(pressure_30))]
Y_30 = [(2.4*pressure_30[i])**0.5 for i in range(len(pressure_30))]
consumption_30 = 0
consumption_30 = 0
for i in range(count):
    # consumption_30 += p*np.pi*dr*(i*dr*((1.7*pressure_30[i])**0.5) +
    #                               (i + 1)*dr*((1.7*pressure_30[i + 1])**0.5))
    consumption_30 += (2*pressure_30[i]*ro)**0.5*np.pi*(2*abs(X_30[i]*deltr) - deltr**2)

pressure_40 = []
with open("40.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_40.append(p)
pressure_40.pop(0)
X_40 = [3 + i*0.45 for i in range(len(pressure_40))]
Y_40 = [(2.4*pressure_40[i])**0.5 for i in range(len(pressure_40))]
consumption_40 = 0
consumption_40 = 0
for i in range(count):
    # consumption_40 += p*np.pi*dr*(i*dr*((1.7*pressure_40[i])**0.5) +
    #                               (i + 1)*dr*((1.7*pressure_40[i + 1])**0.5))
    consumption_40 += (2*pressure_40[i]*ro)**0.5*np.pi*(2*abs(X_40[i]*deltr) - deltr**2)
pressure_50 = []
with open("50.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_50.append(p)

X_50 = [i*0.45 for i in range(len(pressure_50))]
Y_50 = [(2.4*pressure_50[i])**0.5 for i in range(len(pressure_50))]
consumption_50 = 0
for i in range(count):
    # consumption_50 += p*np.pi*dr*(i*dr*((1.7*pressure_50[i])**0.5) +
    #                               (i + 1)*dr*((1.7*pressure_50[i + 1])**0.5))
    consumption_50 += (2*pressure_50[i]*ro)**0.5*np.pi*(2*abs(X_50[i]*deltr) - deltr**2)

pressure_60 = []
with open("60.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_60.append(p)

X_60 = [ 1 + i*0.45 for i in range(len(pressure_60))]
Y_60 = [(2.4*pressure_60[i])**0.5 for i in range(len(pressure_60))]
consumption_60 = 0
for i in range(count):
    # consumption_60 += p*np.pi*dr*(i*dr*((1.7*pressure_60[i])**0.5) +
    #                               (i + 1)*dr*((1.7*pressure_60[i + 1])**0.5))
    consumption_60 += (2*pressure_60[i]*ro)**0.5*np.pi*(2*abs(X_60[i]*deltr) - deltr**2)


pressure_70 = []
with open("70.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_70.append(p)

X_70 = [i*0.45 for i in range(len(pressure_70))]
Y_70 = [(2.4*pressure_70[i])**0.5 for i in range(len(pressure_70))]
consumption_70 = 0
for i in range(count):
    consumption_70 += (2*pressure_70[i]*ro)**0.5*np.pi*(2*abs(X_70[i]*deltr) - deltr**2)


const = 121

for i in range(len(X_00)):
    X_00[i] = X_00[i] - const

for i in range(len(X_10)):
    X_10[i] = X_10[i] - const

for i in range(len(X_00)):
    X_20[i] = X_20[i] - const

for i in range(len(X_30)):
    X_30[i] = X_30[i] - const

for i in range(len(X_40)):
    X_40[i] = X_40[i] - const

for i in range(len(X_50)):
    X_50[i] = X_50[i] - const

for i in range(len(X_60)):
    X_60[i] = X_60[i] - const

for i in range(len(X_70)):
    X_70[i] = X_70[i] - const

fig, ax = plt.subplots(figsize=(12, 8))
consumption = [consumption_00, consumption_10, consumption_20, consumption_30, consumption_40, consumption_50, consumption_60, consumption_70]
consumptionStr = [str(item/10000) for item in consumption]
with open("consumption.txt", "w") as outfile:
    outfile.write("\n".join(consumptionStr))
ax.plot(X_00, Y_00, label='Q(00 мм) = 3.11 г/с ', color='black')
ax.plot(X_10, Y_10, label='Q(10 мм) = 3.17 г/с', color='yellow')
ax.plot(X_20, Y_20, label='Q(20 мм) = 3.96 г/с', color='red')
ax.plot(X_30, Y_30, label='Q(30 мм) = 4.35 г/с', color='green')
ax.plot(X_40, Y_40, label='Q(40 мм) = 4.37 г/с', color='blue')
ax.plot(X_50, Y_50, label='Q(50 мм) = 4.81 г/с', color='purple')
ax.plot(X_60, Y_60, label='Q(60 мм) = 6.03 г/с', color='brown')
ax.plot(X_70, Y_70, label='Q(70 мм) = 6.17 г/с', color='pink')
ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which='minor', linestyle = ':')
ax.set_xlabel("Положение трубки Пито относительно центра струи, мм")
ax.set_ylabel("Скорость воздуха, м/с")
ax.set_title("Скорость потока воздуха в сечении затопленной струи")
ax.legend()
plt.show()
fig.savefig('3.png')


ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which='minor', linestyle = ':')

ax.set_xlabel("Положение трубки Пито относительно центра струи [мм]")
ax.set_ylabel("Скорость воздуха [м/с]")
ax.set_title("Скорость потока воздуха в сечении затопленной струи")


ax.legend()

plt.show()
import WaveFunctions as wave
import numpy as np
import matplotlib.pyplot as plt

path = '/home/gr105/Desktop/RogozinWave/'

data40, duration, count = wave.read(path + 'Calibre40mm.txt')
data60, duration, count = wave.read(path + 'Calibre20mm.txt')
data80, duration, count = wave.read(path + 'Calibre80mm.txt')
data100, duration, count = wave.read(path + 'Calibre100mm.txt')
data120, duration, count = wave.read(path + 'Calibre120mm.txt')

heights = [40, 60, 80, 100, 120]
adc = [np.mean(data40), np.mean(data60), np.mean(data80), np.mean(data100), np.mean(data120)]

# plt.title('Калибровочный график')
# plt.xlabel('Показания АЦП')
# plt.ylabel('h, mm')
# plt.minorticks_on()
# plt.grid(which = "major", linewidth = 1)
# plt.grid(which = "minor", linestyle = '--', linewidth = 0.5)

adclist=np.linspace(np.mean(data40),np.mean(data120),int(np.mean(data120)-np.mean(data40)) + 1)
p = np.polyfit(adc, heights, 2)
# h=[]
# for i in range(int(np.mean(data40)),int(np.mean(data120))):
#     h.append(np.polyval(p,i))
# plt.plot(adclist,h)
#  plt.show()
# plt.savefig('Calibre_plot')

# print(p[0],p[1],p[2])
waveData, duration, count = wave.read(path + 'wave40.txt')

t = np.linspace(0, duration, count)
plt.plot(t[0:60000], waveData[0:60000])
plt.title('Зависимость уровня воды от времени')
plt.xlabel('t, с')
plt.ylabel('h, mm')
plt.minorticks_on()
plt.grid(which = "major", linewidth = 1)
plt.grid(which = "minor", linestyle = '--', linewidth = 0.5)
plt.axvline(x=2.6, ymin=0, ymax=1400, color = 'red')
plt.legend(['Скорость волны'])
plt.savefig('Скорость волны при 40мм.png')
plt.show()

import matplotlib.pyplot as plt;
import matplotlib.ticker as ticker
import numpy as np;
import matplotlib.lines as mlines


data_file = np.loadtxt("data.txt", dtype=int)
settings = np.loadtxt("settings.txt", dtype=float)

fig, ax = plt.subplots(figsize=(16,10), dpi = 300)
time = np.arange(0, settings[0]*(len(data_file)), settings[0])
data_file = data_file * settings[1]

ax.plot(time, data_file, color = 'b', linewidth = 1)
plt.axis([0, 100, 0, 3.5])

plt.ylabel('Voltage, V', fontsize=14)
plt.xlabel('Time, sec', fontsize=14)
plt.title('Charging and discharging a capacitor in an RC circuit', fontsize=14)
plt.text(60, 2.52, 'Charging 45 sec', fontsize=14)
plt.text(60, 2.02, 'Discharging 48 sec', fontsize=14)

ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

#ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
#ax.tick_params(which='major', length=20)
#ax.tick_params(which='minor', length=5)
#plt.yaxis.set_minor_locator(ticker.AutoMinorLocator())
#plt.tick_params(which='major', length=20)
#plt.tick_params(which='minor', length=5)
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

blue_line = mlines.Line2D([], [], color='blue', markersize=30, label='Voltage')
plt.legend(handles=[blue_line])


fig.savefig("graph.svg")
np.save
plt.show()

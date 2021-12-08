import numpy as np
import time
import waveFunctions as b
import matplotlib.pyplot as plt

try:
    data = []
    b.initSpiAdc()
    b.waitForOpen()
    begin = time.time()
    while (time.time() - begin) < 15:
        data.append(b.getAdc())
        #print(b.getAdc())
    finish = time.time()
    time_x = np.linspace(0, 15, len(data))
    b.save(data, begin, finish)
    plt.plot(time_x, data)
    plt.show()
finally:
    b.deinitSpiAdc()


import numpy as np
import pylab as plt

v_time, pressure_1, pressure_2 = np.loadtxt('pressao.txt', unpack=True)

plt.plot(v_time, pressure_1, label='pressure_1')
plt.plot(v_time, pressure_2, label='pressure_2')
plt.yscale('log')

plt.legend()
plt.show()
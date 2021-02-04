import numpy as np
import pylab as plt

magnitude, temperature = np.loadtxt('dados_scatter.txt', unpack=True)

plt.scatter(magnitude, temperature, color='r')
plt.xlabel('Temperature')
plt.ylabel('Magnitude')
plt.legend()
plt.show()
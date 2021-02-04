import numpy as np
import pylab as plt

data = np.arange(0, 1000000)
matrix = np.reshape(data, (1000, 1000))

plt.imshow(matrix)
plt.show()

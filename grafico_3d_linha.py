import numpy as np
import pylab as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
x = np.sin(theta)
y = np.cos(theta)
z = np.arange(0, 2, 0.02)

ax.plot(x, y, z)

plt.show()

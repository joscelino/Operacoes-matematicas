import numpy as np
import pylab as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)

xm, ym = np.meshgrid(x, y)
z = xm ** 2 + ym ** 2

ax.plot_surface(xm, ym, z)
plt.show()

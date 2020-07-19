import numpy as np
import pylab as plt

t = np.arange(0, 1.01, 0.01)
fi = np.pi / 6

v1 = np.sin(2 * np.pi * t)
v2 = np.sin(2 * np.pi * t + fi)

line = plt.plot(t, v1, t, v2)
plt.setp(line[0], label='v1(t)=sin(2.\u03C0.t)', color='r')
plt.setp(line[1], label='v2(t)=sin(2.\u03C0.t + \u03C0/6)', color='b')
plt.title('Wave lag')
plt.legend()
plt.grid()
plt.show()

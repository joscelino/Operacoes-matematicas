import numpy as np
import pylab as plt

theta = np.linspace(0, 4 * np.pi, 50)
f = np.cos(theta)

plt.plot(theta, f, label="f(theta) = cos(theta)")

plt.xlabel('Theta angle')
plt.ylabel('Cos(theta)')
plt.title('Graphic')
plt.legend(loc=1)
plt.show()
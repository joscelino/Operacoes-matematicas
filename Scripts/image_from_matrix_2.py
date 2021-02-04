import numpy as np
import pylab as plt

""" Image with electrical potential of two charges """

df = np.loadtxt('Exemplo_imshow.txt', float)
plt.imshow(df, origin="lower")
plt.hsv()
plt.show()

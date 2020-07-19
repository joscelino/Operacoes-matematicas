import numpy as np

df = np.genfromtxt('exemplo.csv', delimiter=',', skip_header=1, usecols=range(1, 5))

mean_1 = np.mean(df[0,:])
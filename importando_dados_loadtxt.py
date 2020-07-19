import numpy as np

df = np.loadtxt('dados.txt', skiprows=1)

x = df[:, 0]
y = df[:, 1]
z = df[:, 2]

df.shape

a, b, c = np.loadtxt('dados.txt', skiprows=1, unpack=True)

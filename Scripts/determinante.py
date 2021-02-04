import numpy as np

M = np.array([[1, 2], [3, 4]], int)
D = np.linalg.det(M)

M_3 = np.array([[2, 1, 3], [1, -1, 5], [3, 1, -2]], int)
D_3 = np.linalg.det(M_3)
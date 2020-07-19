import numpy as np

I = np.eye(3)

matrix = np.array([[1, 2], [3, 4]], int)

inv_matrix = np.linalg.inv(matrix)
print(inv_matrix)

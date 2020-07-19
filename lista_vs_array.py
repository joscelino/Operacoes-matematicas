import numpy as np
import time

start = time.time()
'''
list = []
for i in range(1, 1000001):
    list.append(i)'''

list2 = np.arange(1, 1000001)
end = time.time()

print('Processing time: ', end - start)

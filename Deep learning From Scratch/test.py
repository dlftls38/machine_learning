import numpy as np
a = np.random.rand(10)

b = np.zeros((10,4))
c = np.zeros((10))
b[np.arange(10),c.flatten()] = a.flatten()
print(b)
print("--------------------------------------------------------")
print(a)